#!/usr/bin/env python3
"""Genera el reporte; añade --con-presentacion para generar también PDF y web de las diapositivas."""

import argparse
import html
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
from contenido import leer_referencias, preparar_referencias, verificar_laminas


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
    "Firma": "NombreFirma",
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
    return fields, members


def render_tex(fields, members):
    lines = ["% Generado por compilar.py desde datos.md. No editar."]
    lines += [rf"\newcommand{{\{macro}}}{{{tex_escape(fields[key])}}}" for key, macro in FIELDS.items()]
    rows = [" & ".join(map(tex_escape, member)) + r" \\" for member in members]
    lines.append("\\newcommand{\\Integrantes}{%\n" + "\n".join(rows) + "\n}")
    return "\n".join(lines) + "\n"


def render_web(fields, members):
    """Actualiza solo marcadores de datos; conserva las diapositivas editables."""
    source = (ROOT / "reveal.js/index.html").read_text(encoding="utf-8")

    def replace_field(match):
        key = match.group(2)
        if key not in FIELDS or key == "Firma":
            raise ValueError(f"Marcador web no permitido: {key}")
        return match.group(1) + html.escape(fields[key]) + match.group(3)

    source = re.sub(
        r'(<span data-campo="([^"]+)">).*?(</span>)',
        replace_field, source, flags=re.DOTALL,
    )
    rows = "\n".join(
        "<tr>" + "".join(f"<td>{html.escape(cell)}</td>" for cell in row) + "</tr>"
        for row in members
    )
    source, count = re.subn(
        r'(<tbody id="integrantes">).*?(</tbody>)',
        lambda match: match.group(1) + "\n" + rows + "\n" + match.group(2),
        source, flags=re.DOTALL,
    )
    if count != 1:
        raise ValueError('El HTML debe contener un único <tbody id="integrantes">.')
    source = re.sub(r"<title>.*?</title>", lambda _: "<title>" + html.escape(fields["Título"]) + "</title>", source, count=1, flags=re.DOTALL)
    return source


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
    parser.add_argument("--con-presentacion", action="store_true", help="Incluir explícitamente la presentación PDF y sincronizar su HTML, además del reporte.")
    parser.add_argument("--verificar", action="store_true", help="Comprobar coherencia y referencias sin compilar ni modificar entregables.")
    args = parser.parse_args()
    fields, members = read_data()
    data = render_tex(fields, members)
    web = render_web(fields, members) if args.con_presentacion else None
    reporte = (ROOT / "reporte.tex").read_text(encoding="utf-8")
    presentacion = (ROOT / "presentacion.tex").read_text(encoding="utf-8") if args.con_presentacion else ""
    tex_sources = [presentacion, reporte]
    refs = leer_referencias(ROOT / "referencias.json")
    web, citas, bibliografia, referencias_slides = preparar_referencias(refs, tex_sources, web, tex_escape)
    if args.con_presentacion:
        count = verificar_laminas(presentacion, web, fields)
        print(f"Coherencia verificada: {count} láminas, títulos y expositores coinciden.", flush=True)
    else:
        print("Modo reporte: la presentación PDF y el HTML no se procesan.", flush=True)
    if any(entry.get("ejemplo") for entry in refs.values()):
        print("AVISO: la bibliografía conserva referencias de ejemplo; no es un trabajo terminado.", flush=True)
    if args.verificar:
        print("Referencias y citas verificadas. No se modificaron los entregables.", flush=True)
        return
    for resource in ("assets/img/institucional/isotipo-azul.png", "assets/img/institucional/logo-facultad.png", "assets/img/institucional/acreditacion.png", "assets/fonts/firma.otf"):
        if not (ROOT / resource).is_file():
            raise FileNotFoundError(f"Falta un recurso institucional: {resource}")
    build = ROOT / ".build"
    build.mkdir(exist_ok=True)
    (build / "datos.tex").write_text(data, encoding="utf-8")
    generated = [("citas.tex", citas), ("referencias-reporte.tex", bibliografia)]
    if args.con_presentacion:
        generated.append(("referencias-presentacion.tex", referencias_slides))
    for filename, content in generated:
        (build / filename).write_text(content, encoding="utf-8")
    compiler = get_compiler(args.sin_red)
    # Una salida nueva evita confundir archivos de una ejecución anterior con los actuales.
    with tempfile.TemporaryDirectory(prefix="pdf-", dir=build) as staging:
        documents = ("presentacion", "reporte") if args.con_presentacion else ("reporte",)
        for name in documents:
            print(f"\nCompilando {name}.tex…", flush=True)
            command = [str(compiler), "--untrusted", "--keep-logs", "--outdir", staging]
            if args.sin_red:
                command.append("--only-cached")
            command.append(str(ROOT / f"{name}.tex"))
            result = subprocess.run(command, cwd=ROOT)
            log = Path(staging) / f"{name}.log"
            if log.exists():
                shutil.copy2(log, build / log.name)
            if result.returncode:
                raise RuntimeError(f"Falló {name}.tex. Revisa .build/{name}.log. Los PDF anteriores no se actualizaron.")
            pdf = Path(staging) / f"{name}.pdf"
            if not pdf.is_file() or not pdf.read_bytes().startswith(b"%PDF-"):
                raise RuntimeError(f"No se generó un PDF válido para {name}.")
        destination = ROOT / "pdf"
        destination.mkdir(exist_ok=True)
        for name in documents:
            shutil.copy2(Path(staging) / f"{name}.pdf", destination / f"{name}.pdf")
            print(f"PDF actualizado: pdf/{name}.pdf", flush=True)
        if args.con_presentacion:
            (ROOT / "reveal.js/index.html").write_text(web, encoding="utf-8")
            print("Datos web actualizados: reveal.js/index.html", flush=True)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError, StopIteration, tarfile.TarError, zipfile.BadZipFile) as error:
        print(f"\nERROR: {error}", file=sys.stderr)
        sys.exit(1)
