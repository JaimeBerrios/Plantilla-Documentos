# Plantilla de Propuesta de Proyecto · UNAB

Una base para preparar la **Ficha de Propuesta de Proyecto (Fase 1)** con Codex para la Universidad Dr. Andrés Bello, reproduciendo fielmente el formato técnico oficial de validación docente en un máximo de dos páginas.

El entregable generado es **`pdf/propuesta.pdf`**.

## Tu flujo de trabajo

1. Clona el repositorio y ábrelo en VS Code.
2. Crea una rama desde la plantilla base para cada propuesta:

   ```bash
   git switch main
   git switch -c propuesta/nombre-del-proyecto
   ```

   Si tu rama base tiene otro nombre, úsalo en lugar de `main`. Guarda los cambios del trabajo anterior antes de cambiar de rama.
3. Completa **[datos.md](datos.md)**: asignatura, docente, fecha, integrantes (hasta 4 estudiantes con carnet), título de la propuesta y datos preliminares.
4. Pídele a Codex:

   > Lee AGENTS.md y datos.md. Prepara la ficha técnica de propuesta de proyecto en propuesta.tex, asegurando el formato oficial de la guía en un máximo de 2 páginas. Compila pdf/propuesta.pdf y verifica que no existan desbordes ni tablas cortadas.

5. Abre **[propuesta PDF](pdf/propuesta.pdf)**. El archivo inicial contiene campos y espacios claramente identificados para completar con la investigación de tu proyecto.
6. Guarda las fuentes y el PDF en la misma rama. Sube esa rama a GitHub cuando quieras respaldarla; la compilación se ejecuta localmente.

## Compilación automática

Codex debe ejecutar desde la raíz:

```bash
python3 compilar.py
```

En Windows: `python compilar.py`. Requiere **Python 3.9 o posterior**; no necesita paquetes de pip. En VS Code también puedes usar **Terminal → Ejecutar tarea de compilación** (`Ctrl+Shift+B`), que genera el documento mediante la tarea configurada.

La primera ejecución descarga **Tectonic 0.15.0** desde su distribución oficial. Se guarda fuera del repositorio, en la carpeta de datos del usuario:

| Sistema | Carpeta del compilador |
|---|---|
| Linux | `~/.local/share/plantilla-unab/tectonic-0.15.0/` (respeta `XDG_DATA_HOME`) |
| macOS | `~/Library/Application Support/plantilla-unab/tectonic-0.15.0/` |
| Windows | `%LOCALAPPDATA%/plantilla-unab/tectonic-0.15.0/` |

El mismo usuario reutiliza esa instalación en todas sus ramas y clones. Tectonic conserva además su propia caché de paquetes. Necesitas conexión la primera vez y cuando un documento requiera paquetes nuevos. Para usar solo lo descargado:

```bash
python3 compilar.py --sin-red
```

La instalación automática contempla Linux y macOS de 64 bits (Intel/AMD y ARM) y Windows x64. Si Codex solicita acceso de red o escritura a la carpeta de usuario, es para preparar o reutilizar ese entorno local.

Los datos generales y los integrantes de `datos.md` se incorporan automáticamente al documento. El resto del archivo es una guía para Codex: compilar no redacta ni investiga el contenido por sí solo.

Solo cuando el documento compila correctamente se actualiza `pdf/propuesta.pdf`. Si hay un error, el comando termina con error y conserva la versión anterior; revisa el registro en `.build/propuesta.log` antes de entregar el trabajo.

## Estructura de la Ficha Técnica (Fase 1)

El documento cumple con el límite estricto de **dos páginas**:

- **Página 1**:
  - Encabezado institucional con ambos logos (`assets/img/logo-unab-guia.png` y `assets/img/logo-facultad.png`), asignatura y fecha.
  - Título del proyecto y tabla de miembros del equipo (Líder y hasta 3 estudiantes con carnet).
  - Problemática Ambiental Identificada y Justificación.
  - Población Objetivo y Beneficiarios Directos.
- **Página 2**:
  - Diagrama de bloques preliminar del sistema (Sensores $\rightarrow$ Lógica Combinacional / MUX / DEMUX $\rightarrow$ Arduino $\rightarrow$ Actuadores).
  - Presupuesto estimado y lista de materiales a utilizar (cantidades, descripción, aplicación y costos unitario/total).
  - Firmas de conformidad del líder del equipo y sección reservada para validación, dictamen y sello del catedrático.

## Archivos que se conservan

```text
datos.md                         Datos y consigna de la propuesta
propuesta.tex                    Contenido editable de la ficha de propuesta en LaTeX
compilar.py                      Descarga inicial y compilación de pdf/propuesta.pdf
AGENTS.md                        Instrucciones para Codex
README.md                        Esta guía
plantilla/unab_propuesta.sty     Estilo institucional y configuración visual
assets/img/                      Logos institucionales e imágenes del proyecto
pdf/propuesta.pdf                Ficha técnica de propuesta lista para entregar
.vscode/tasks.json               Compilación desde VS Code
```

Edita normalmente `datos.md` y deja que Codex trabaje en `propuesta.tex`. Puedes agregar diagramas o esquemas en `assets/img/`. Los dos logos siempre se conservan.

`.build/` contiene datos generados y registros; está excluida de Git. El PDF `pdf/propuesta.pdf` sí se versiona, para que cada rama conserve su entregable. Si existe un archivo anterior `pdf/reporte.pdf`, este corresponde a la versión previa y no forma parte de la entrega actual.

Referencias técnicas: [Tectonic](https://tectonic-typesetting.github.io/en-US/install.html) y [las instrucciones AGENTS.md de Codex](https://developers.openai.com/codex/guides/agents-md).
