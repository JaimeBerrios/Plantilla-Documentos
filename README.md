# Plantilla académica · UNAB

Una base para preparar **presentaciones y reportes con Codex**, conservando los
logos de la Universidad Dr. Andrés Bello, el azul institucional y la firma
personal al final del reporte.

## Tu flujo de trabajo

1. Clona el repositorio y ábrelo en VS Code.
2. Crea una rama desde la plantilla base para cada trabajo:

   ```bash
   git switch main
   git switch -c materia/nombre-del-proyecto
   ```

   Si tu rama base tiene otro nombre, úsalo en lugar de `main`. Guarda los cambios
   del trabajo anterior antes de cambiar de rama.
3. Completa **[datos.md](datos.md)**: docente, asignatura, integrantes, tema,
   indicaciones y fuentes.
4. Pídele a Codex:

   > Lee AGENTS.md y datos.md. Prepara el reporte y la presentación para este
   > trabajo, conserva la identidad de la universidad y la firma al final del
   > reporte. Compila los dos PDF, revisa que no haya texto cortado y entrégamelos.

5. Abre **[presentación](pdf/presentacion.pdf)** y **[reporte](pdf/reporte.pdf)**.
   Los archivos iniciales son ejemplos editables, no una investigación terminada.
6. Guarda las fuentes y los PDF en la misma rama. Sube esa rama a GitHub cuando
   quieras respaldarla; la compilación funciona localmente.

## Compilación automática

Codex debe ejecutar desde la raíz:

```bash
python3 compilar.py
```

En Windows: `python compilar.py`. Requiere **Python 3.9 o posterior**; no necesita
paquetes de pip. En VS Code también puedes usar **Terminal → Ejecutar tarea de
compilación** (`Ctrl+Shift+B`), que genera ambos documentos con el mismo script.

La primera ejecución descarga **Tectonic 0.15.0** desde su distribución oficial.
Se guarda fuera del repositorio, en la carpeta de datos del usuario:

| Sistema | Carpeta del compilador |
|---|---|
| Linux | `~/.local/share/plantilla-unab/tectonic-0.15.0/` (respeta `XDG_DATA_HOME`) |
| macOS | `~/Library/Application Support/plantilla-unab/tectonic-0.15.0/` |
| Windows | `%LOCALAPPDATA%/plantilla-unab/tectonic-0.15.0/` |

El mismo usuario reutiliza esa instalación en todas sus ramas y clones. Tectonic
conserva además su propia caché de paquetes. Necesitas conexión la primera vez
y cuando un documento requiera paquetes nuevos. Para usar solo lo descargado:

```bash
python3 compilar.py --sin-red
```

La instalación automática contempla Linux y macOS de 64 bits (Intel/AMD y ARM)
y Windows x64. Si Codex solicita acceso de red o escritura a la carpeta de
usuario, es para preparar o reutilizar ese entorno local.

Los datos generales y los integrantes de `datos.md` se incorporan automáticamente
a ambos documentos. El resto del archivo es una guía para Codex: compilar no
redacta ni investiga el contenido por sí solo.

Solo cuando ambos documentos compilan correctamente se actualizan los PDF de
`pdf/`. Si hay un error, el comando termina con error y conserva las versiones
anteriores; revisa los registros en `.build/` antes de entregar el trabajo.

## Archivos que se conservan

```text
datos.md                         Datos y consigna del trabajo
presentacion.tex                 Contenido de las diapositivas
reporte.tex                      Contenido del documento
compilar.py                      Descarga inicial y compilación de ambos PDF
AGENTS.md                        Instrucciones para Codex
README.md                        Esta guía
plantilla/                       Dos estilos institucionales reutilizables
assets/img/                      Logo de la universidad y de la facultad
assets/fonts/firma.otf           Fuente original de la firma
pdf/                             Presentación y reporte listos para abrir
.vscode/tasks.json               Compilación desde VS Code
```

Edita normalmente `datos.md` y deja que Codex trabaje en los dos `.tex`. Puedes
agregar imágenes de apoyo en `assets/img/`. Los dos logos siempre se conservan.
La firma toma el texto del campo `Firma` y solo aparece al final del reporte.

`.build/` contiene datos generados y registros; está excluida de Git. Los PDF sí
se versionan, para que cada rama conserve sus entregables. No se necesita HTML,
GitHub Actions ni una distribución LaTeX completa instalada manualmente.

Referencias técnicas: [Tectonic](https://tectonic-typesetting.github.io/en-US/install.html)
y [las instrucciones AGENTS.md de Codex](https://developers.openai.com/codex/guides/agents-md).
