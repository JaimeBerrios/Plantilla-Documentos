#!/usr/bin/env python3
"""Genera los dos PDF con Tectonic; solo requiere Python 3.9 o posterior."""

import argparse
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
import zipfile


ROOT = Path(__file__).resolve().parent
VERSION = "0.15.0"  # Versión fija para reutilizar el mismo motor entre ramas.
FIELDS = {
    "Título": "TituloTrabajo",
    "Subtítulo": "SubtituloTrabajo",
    "Título corto": "TituloCorto",
    "Institución": "Institucion",
    "Facultad": "Facultad",
    "Asignatura": "Asignatura",
    "Docente": "Docente",
    "Grupo": "Grupo",
    "Lugar y fecha": "LugarFecha",
    "Sede": "Sede",
    "Carrera": "Carrera",
}


def tex_escape(value):
    replacements = {
        "\\": r"\textbackslash{}", "{": r"\{", "}": r"\}",
        "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
        "_": r"\_", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in value)


def read_data():
    fields, members = {}, []
    section = ""
    for line in (ROOT / "datos.md").read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
        elif section == "Datos generales":
            match = re.fullmatch(r"- ([^:]+):\s*(.*)", line)
            if match:
                key, value = match.groups()
                if key in fields:
                    raise ValueError(f"Campo repetido en datos.md: {key}")
                fields[key] = value.strip()
        elif section == "Integrantes" and line.strip().startswith("|"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if cells == ["Nombre", "Código"] or all(re.fullmatch(r":?-+:?", c) for c in cells):
                continue
            if len(cells) != 2 or not all(cells):
                raise ValueError("Cada integrante debe tener Nombre y Código en datos.md.")
            members.append(cells)
    missing = [key for key in FIELDS if not fields.get(key)]
    if missing:
        raise ValueError("Completa estos campos de datos.md: " + ", ".join(missing))
    if not members:
        raise ValueError("Agrega al menos un integrante en datos.md.")
    lines = ["% Generado por compilar.py desde datos.md. No editar."]
    lines += [rf"\newcommand{{\{macro}}}{{{tex_escape(fields[key])}}}" for key, macro in FIELDS.items()]
    rows = [" & ".join(map(tex_escape, member)) + r" \\" for member in members]
    lines.append("\\newcommand{\\Integrantes}{%\n" + "\n".join(rows) + "\n}")
    return "\n".join(lines) + "\n"


def compiler_directory():
    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA", str(Path.home() / "AppData/Local")))
    elif sys.platform == "darwin":
        base = Path.home() / "Library/Application Support"
    else:
        base = Path(os.environ.get("XDG_DATA_HOME", str(Path.home() / ".local/share")))
    return base / "plantilla-unab" / f"tectonic-{VERSION}"


def get_compiler(offline=False):
    executable = "tectonic.exe" if sys.platform == "win32" else "tectonic"
    target = compiler_directory() / executable
    if target.is_file():
        print(f"Reutilizando compilador: {target}", flush=True)
        return target
    if offline:
        raise RuntimeError("Primera ejecución: compila con conexión, sin --sin-red.")
    machine = platform.machine().lower()
    arch = {"amd64": "x86_64", "arm64": "aarch64"}.get(machine, machine)
    platforms = {
        ("linux", "x86_64"): "x86_64-unknown-linux-musl",
        ("linux", "aarch64"): "aarch64-unknown-linux-musl",
        ("darwin", "x86_64"): "x86_64-apple-darwin",
        ("darwin", "aarch64"): "aarch64-apple-darwin",
        ("win32", "x86_64"): "x86_64-pc-windows-msvc",
    }
    triplet = platforms.get((sys.platform, arch))
    if not triplet:
        raise RuntimeError(f"Instalación automática no disponible para {sys.platform}/{arch}.")
    extension = "zip" if sys.platform == "win32" else "tar.gz"
    asset = f"tectonic-{VERSION}-{triplet}.{extension}"
    url = f"https://github.com/tectonic-typesetting/tectonic/releases/download/tectonic%40{VERSION}/{asset}"
    print(f"Descargando Tectonic {VERSION} desde su distribución oficial…", flush=True)
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=target.parent) as staging:
        archive = Path(staging) / asset
        request = urllib.request.Request(url, headers={"User-Agent": "plantilla-unab"})
        with urllib.request.urlopen(request, timeout=120) as response, archive.open("wb") as output:
            shutil.copyfileobj(response, output)
        binary = Path(staging) / executable
        # Extraer únicamente el ejecutable, sin aceptar rutas del archivo descargado.
        if extension == "zip":
            with zipfile.ZipFile(archive) as package:
                entry = next(name for name in package.namelist() if Path(name).name == executable)
                binary.write_bytes(package.read(entry))
        else:
            with tarfile.open(archive) as package:
                entry = next(item for item in package.getmembers() if item.isfile() and Path(item.name).name == executable)
                with package.extractfile(entry) as source, binary.open("wb") as output:
                    shutil.copyfileobj(source, output)
        binary.chmod(0o755)
        subprocess.run([str(binary), "--version"], check=True)
        os.replace(binary, target)
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sin-red", action="store_true", help="Usar solo el motor y los paquetes ya descargados.")
    args = parser.parse_args()
    data = read_data()
    for resource in ("assets/img/logo-unab.png", "assets/img/logo-facultad.png"):
        if not (ROOT / resource).is_file():
            raise FileNotFoundError(f"Falta un recurso institucional: {resource}")
    build = ROOT / ".build"
    build.mkdir(exist_ok=True)
    (build / "datos.tex").write_text(data, encoding="utf-8")
    compiler = get_compiler(args.sin_red)
    # Una salida nueva evita confundir archivos de una ejecución anterior con los actuales.
    with tempfile.TemporaryDirectory(prefix="pdf-", dir=build) as staging:
        print("\nCompilando reporte.tex…", flush=True)
        command = [str(compiler), "--untrusted", "--keep-logs", "--outdir", staging]
        if args.sin_red:
            command.append("--only-cached")
        command.append(str(ROOT / "reporte.tex"))
        result = subprocess.run(command, cwd=ROOT)
        log = Path(staging) / "reporte.log"
        if log.exists():
            shutil.copy2(log, build / log.name)
        if result.returncode:
            raise RuntimeError("Falló reporte.tex. Revisa .build/reporte.log. El PDF anterior no se actualizó.")
        pdf = Path(staging) / "reporte.pdf"
        if not pdf.is_file() or not pdf.read_bytes().startswith(b"%PDF-"):
            raise RuntimeError("No se generó un PDF válido para el reporte.")
        destination = ROOT / "pdf"
        destination.mkdir(exist_ok=True)
        # Limpiar PDF antiguos para dejar únicamente el entregable solicitado
        for old_pdf in destination.glob("*.pdf"):
            if old_pdf.name != "Entregable2.pdf":
                old_pdf.unlink(missing_ok=True)
        shutil.copy2(pdf, destination / "Entregable2.pdf")
        print("PDF actualizado: pdf/Entregable2.pdf", flush=True)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError, StopIteration, tarfile.TarError, zipfile.BadZipFile) as error:
        print(f"\nERROR: {error}", file=sys.stderr)
        sys.exit(1)
