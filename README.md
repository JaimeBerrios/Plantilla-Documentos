# Plantilla académica · UNAB

Una base para preparar **proyectos de investigación con Codex**, conservando los
logos de la Universidad Dr. Andrés Bello y la estructura académica formal.

## Variables de la Investigación

A partir de la estructuración del proyecto *"Diseño de un marco de trabajo basado en Spec-Driven Development (SDD) para el aseguramiento de la calidad en la automatización de procesos empresariales con IA"*, se han definido las siguientes variables:

*   **Variable Independiente (Causa):** El marco de trabajo basado en *Spec-Driven Development* (uso de especificaciones formales innegociables y reglas estrictas).
*   **Variable Dependiente (Efecto):** El aseguramiento de la calidad técnica (reducción de deuda técnica, mitigación de alucinaciones y aumento del determinismo en la generación de código empresarial).

## Guion sugerido para presentar a la Licenciada

Si vas a leer o exponer el avance, aquí tienes un guion mucho más natural y conversacional, centrado en "vender" la idea principal sin aburrir leyendo la teoría. 

> **1. Saludo e introducción (Portada)**
> "Buenos días, Licenciada y compañeros. Como equipo, queremos presentarles la idea central de nuestro proyecto de investigación, que se titula: *Diseño de un marco de trabajo basado en Spec-Driven Development (SDD) para el aseguramiento de la calidad en la automatización de procesos empresariales con IA*."
> 
> **2. El Problema y la Justificación (De forma breve)**
> "El proyecto nace de un problema muy actual: hoy en día, las empresas están usando Inteligencia Artificial para escribir código y automatizar procesos, pero lo intentan hacer usando metodologías ágiles tradicionales como Scrum. El problema es que, al darle a la IA historias de usuario ambiguas, la IA empieza a tomar sus propias decisiones, alucina y genera código inestable. A esto se le llama *Vibe Coding*, y está creando una inmensa deuda técnica. Nuestro enfoque justifica que el desarrollador ya no debe ser un 'digitador', sino un arquitecto de software."
> 
> **3. La Solución (Nuestros objetivos)**
> "Para resolver esto, nuestro objetivo principal es proponer un marco de trabajo estructurado en *Spec-Driven Development*. Es decir, establecer reglas innegociables y especificaciones estrictas antes de que la IA genere siquiera una línea de código."
> 
> **4. Presentación de las Variables**
> *(Nota: Este es el momento ideal para mencionar las variables, ya que acabas de explicar la causa y el efecto de tu investigación).*
> "A partir de esto, tenemos muy claras nuestras variables de estudio:
> Nuestra **variable independiente**, es decir la causa o herramienta, es la *implementación de este marco de trabajo SDD*. 
> Por otro lado, nuestra **variable dependiente**, que es el impacto que buscamos, es *el aseguramiento de la calidad técnica*, reduciendo las alucinaciones y garantizando que el código final sea totalmente seguro para las empresas."
> 
> **5. Cierre**
> "Actualmente ya estructuramos el planteamiento, la justificación y los objetivos bajo esta premisa. Estaríamos listos para recibir sus observaciones y arrancar con el marco teórico y la metodología."

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

   > Lee AGENTS.md y datos.md. Prepara el reporte y la presentación (PDF y web)
   > para este trabajo, conserva la identidad de la universidad. Compila los 
   > dos PDF, revisa que no haya texto cortado y entrégamelos.

5. Abre **[presentación PDF](pdf/presentacion.pdf)**, **[reporte PDF](pdf/reporte.pdf)** 
   y **[presentación web](reveal.js/index.html)**.
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
reveal.js/                       Plantilla de presentación web interactiva
.vscode/tasks.json               Compilación desde VS Code
```

Edita normalmente `datos.md` y deja que Codex trabaje en los dos `.tex`. Puedes
agregar imágenes de apoyo en `assets/img/`. Los dos logos siempre se conservan.

`.build/` contiene datos generados y registros; está excluida de Git. Los PDF sí
se versionan, para que cada rama conserve sus entregables. No se necesita HTML,
GitHub Actions ni una distribución LaTeX completa instalada manualmente.

Referencias técnicas: [Tectonic](https://tectonic-typesetting.github.io/en-US/install.html)
y [las instrucciones AGENTS.md de Codex](https://developers.openai.com/codex/guides/agents-md).
