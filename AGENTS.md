# Instrucciones para Codex

## Propósito y archivos

Este repositorio es una plantilla local para la **Fase 1: Ficha de Propuesta de Proyecto**
del entregable académico UNAB: `pdf/propuesta.pdf`. GitHub aloja las ramas; no compila.
Lee `datos.md` antes de editar y revisa el estado de Git para respetar el trabajo
existente. Trabaja en la rama actual. Si el usuario pide una rama nueva, créala
con un nombre descriptivo; no cambies de rama ni publiques cambios por rutina.

- `datos.md`: fuente compartida de datos e indicaciones del proyecto en español.
- `propuesta.tex`: contenido editable de la ficha de propuesta en LaTeX.
- `plantilla/unab_propuesta.sty`: diseño reutilizable y estilos técnicos basados en la guía oficial.
- `assets/img/`: logos institucionales (`assets/img/logo-unab-guia.png`, `assets/img/logo-facultad.png`) e imágenes complementarias.
- `compilar.py`: único punto de entrada para compilar `pdf/propuesta.pdf`.

## Edición

Conserva los encabezados y las etiquetas de datos generales de `datos.md`, y las
columnas Nombre/Código. El script escapa caracteres especiales y genera
`.build/datos.tex`; no edites ese archivo ni dupliques estos valores manualmente.
Los apartados de problemática, justificación, población objetivo, diagrama de bloques
y presupuesto requieren interpretación y redacción técnica; no se convierten
automáticamente en contenido académico.

Usa los datos y fuentes proporcionados. No inventes integrantes, códigos, nombres
de docentes, resultados, presupuesto ni población beneficiaria. Si falta información
esencial, pregunta; puedes avanzar con las partes independientes. En un borrador
identifica claramente lo pendiente. Sustituye los textos de ejemplo cuando prepares un
trabajo real y adapta las secciones a la consigna.

Conserva ambos logos institucionales, sus proporciones y el azul institucional `#173864`.
El documento debe ajustarse estrictamente a un **máximo de dos páginas**, conforme a la
guía técnica:
- **Página 1**: Encabezado institucional, Título e Integrantes (hasta 4 estudiantes con carnet),
  Problemática Ambiental Identificada, Justificación y Población Objetivo y Beneficiarios Directos.
- **Página 2**: Diagrama de bloques preliminar del sistema (Sensores $\rightarrow$ Lógica Combinacional / MUX / DEMUX $\rightarrow$ Arduino $\rightarrow$ Actuadores),
  Presupuesto estimado y lista de materiales a utilizar, y recuadro de Firmas de conformidad y
  validación docente (con dictamen y observaciones).

Las firmas deben ser espacios en blanco para firma física y sello docente conforme a la
guía, no una firma tipográfica personal.

## Compilación y entrega obligatorias

Después de editar contenido o diseño, ejecuta `python3 compilar.py` desde la raíz
(en Windows, `python compilar.py`). El script descarga una versión fija de
Tectonic si falta en la carpeta de datos del usuario y la reutiliza en futuras
ramas y clones. No instales una copia por proyecto ni guardes el compilador en Git.
La primera ejecución y los paquetes nuevos necesitan red. Respeta los permisos
del entorno y solicita la autorización técnica necesaria si el sandbox bloquea
red o escritura fuera del repositorio; no eludas esas restricciones.

1. Compila la propuesta con el script y corrige errores.
2. Revisa `.build/propuesta.log`: resuelve referencias indefinidas, caracteres
   faltantes y desbordamientos visibles (overfull/underfull).
3. Inspecciona el PDF resultante: logos completos y proporcionales, encabezado legible,
   tablas sin cortes ni desbordes, espacios de firma utilizables y estricto límite de 2 páginas.
   Si hay herramientas de renderizado, guarda las capturas temporales en `.build/` o fuera
   del repositorio.
4. Entrega el enlace a `pdf/propuesta.pdf`, señala las fuentes editables y resume
   brevemente los cambios y verificaciones realizadas.

No declares la tarea terminada con PDF antiguos. Si permanece un archivo anterior como
`pdf/reporte.pdf`, identifícalo como un archivo previo; el entregable actual es exclusivamente
`pdf/propuesta.pdf`.
`--sin-red` permite comprobar que el motor y los paquetes se reutilizan sin descargas.
Conserva las fuentes necesarias para seguir editando. No hagas commit ni push salvo que se solicite.
