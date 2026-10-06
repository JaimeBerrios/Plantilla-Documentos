# Instrucciones para Codex

## Propósito y archivos

Este repositorio es una plantilla local para tres entregables académicos UNAB:
`pdf/presentacion.pdf`, `pdf/reporte.pdf` y `reveal.js/index.html`. GitHub aloja las ramas; no compila.
Lee `datos.md` antes de editar y revisa el estado de Git para respetar el trabajo
existente. Trabaja en la rama actual. Si el usuario pide una rama nueva, créala
con un nombre descriptivo; no cambies de rama ni publiques cambios por rutina.

- `datos.md`: fuente compartida de datos y consigna en español.
- `presentacion.tex`, `reporte.tex` y `reveal.js/index.html`: contenido editable de cada entregable.
- `plantilla/*.sty` y `reveal.js/plantilla.html`: diseño reutilizable; modificar solo si hace falta ajustar
  la presentación visual o si el usuario lo solicita.
- `assets/img/`: logos obligatorios e imágenes adicionales.
- `assets/fonts/firma.otf`: fuente personal original, usada solo por el reporte.
- `compilar.py`: único punto de entrada para compilar los dos documentos.

## Edición

Conserva los encabezados y las etiquetas de datos generales de `datos.md`, y las
columnas Nombre/Código. El script escapa caracteres especiales y genera
`.build/datos.tex`; no edites ese archivo ni dupliques estos valores en los `.tex`.
Los apartados de tema, indicaciones y fuentes requieren interpretación y redacción;
no se convierten automáticamente en contenido académico.

Usa los datos y fuentes proporcionados. No inventes integrantes, códigos, nombres
de docentes, resultados ni referencias. Si falta información esencial, pregunta;
puedes avanzar con las partes independientes. En un borrador identifica lo pendiente.
Sustituye los textos de ejemplo cuando prepares un trabajo real y adapta las
secciones a la consigna. Mantén coherencia entre reporte y presentación.

Conserva ambos logos, sus proporciones y el azul institucional `#173864`.
Mantén diapositivas 16:9, textos breves y un pie con el expositor correspondiente.
No reduzcas indiscriminadamente el tamaño de letra para hacer caber contenido:
divide láminas o reorganiza la portada si hay muchos integrantes o títulos largos.
El reporte usa tamaño carta. Cuando prepares la presentación, asegúrate de reflejar los cambios
tanto en `presentacion.tex` como en `reveal.js/index.html`.

## Compilación y entrega obligatorias

Después de editar contenido o diseño, ejecuta `python3 compilar.py` desde la raíz
(en Windows, `python compilar.py`). El script descarga una versión fija de
Tectonic si falta en la carpeta de datos del usuario y la reutiliza en futuras
ramas y clones. No instales una copia por proyecto ni guardes el compilador en Git.
La primera ejecución y los paquetes nuevos necesitan red. Respeta los permisos
del entorno y solicita la autorización técnica necesaria si el sandbox bloquea
red o escritura fuera del repositorio; no eludas esas restricciones.

1. Compila ambos documentos con el script y corrige errores.
2. Revisa `.build/presentacion.log` y `.build/reporte.log`: resuelve referencias
   indefinidas, caracteres faltantes y desbordamientos visibles.
3. Inspecciona los PDF: logos completos, portada legible, tablas y pies sin cortes
   y numeración coherente. Si hay herramientas de
   renderizado, guarda las capturas temporales en `.build/` o fuera del repositorio.
4. Entrega enlaces a los dos PDF, al HTML web y un resumen breve de los cambios y verificaciones.

No declares la tarea terminada con PDF antiguos ni sustituyas LaTeX por una impresión PDF desde HTML.
Si la compilación queda bloqueada, explica el error y distingue los PDF anteriores de los nuevos. El script conserva los anteriores si uno falla.
`--sin-red` permite comprobar que el motor y los paquetes se reutilizan sin descargas.
Los entregables finales son los dos PDF y `reveal.js/index.html`; conserva también las fuentes
necesarias para seguir editándolos. No hagas commit ni push salvo que se solicite.
