# Instrucciones para Codex

## Propósito y archivos

Este repositorio es una plantilla local para tres entregables académicos UNAB:
`pdf/presentacion.pdf`, `pdf/reporte.pdf` y `reveal.js/index.html`. GitHub aloja las ramas; no compila.
**Por defecto, prepara, genera y compila exclusivamente el reporte.**
Solo prepara o actualiza `presentacion.tex`, `pdf/presentacion.pdf` y
`reveal.js/index.html` cuando el usuario solicite explícitamente la presentación.
Para incluirla, ejecuta `python compilar.py --con-presentacion`.
Lee `datos.md` antes de editar y revisa el estado de Git para respetar el trabajo
existente. Trabaja en la rama actual. Si el usuario pide una rama nueva, créala
con un nombre descriptivo; no cambies de rama ni publiques cambios por rutina.

- `datos.md`: fuente compartida de datos y consigna en español.
- `referencias.json`: referencias redactadas en APA 7 y formas de cita compartidas.
- `contenido.py`: comprobación de láminas y generación de citas/bibliografías.
- `presentacion.tex`, `reporte.tex` y `reveal.js/index.html`: contenido editable de cada entregable.
- `plantilla/*.sty`, `reveal.js/css/unab.css` y `reveal.js/js/presentacion.js`: diseño reutilizable; modificar solo si hace falta ajustar
  la presentación visual o si el usuario lo solicita.
- `assets/img/institucional/`: logos obligatorios, variantes y acreditación.
- `assets/img/contenido/`: imágenes y gráficos del trabajo.
- `vendor/reveal.js/`: biblioteca externa con su versión y licencia; no personalizar aquí.
- `index.html` y `web/`: guía web; mantenerla coherente con README.md y compilar.py.
- `assets/fonts/firma.otf`: fuente personal original, usada solo por el reporte.
- `compilar.py`: único punto de entrada para compilar los dos documentos y sincronizar datos web.

## Edición

Conserva los encabezados y las etiquetas de datos generales de `datos.md`, y las
columnas Nombre/Código. El script escapa caracteres especiales y genera
`.build/datos.tex`; no edites ese archivo ni dupliques estos valores en los `.tex`.
Solo con `--con-presentacion`, también actualiza los elementos `span[data-campo]` y `tbody#integrantes` del HTML;
conserva esos marcadores y edita sus valores en datos.md. La firma no se exporta al HTML.
Conserva también los marcadores `data-cita` y `referencias:inicio` / `referencias:fin`.
Las citas se editan en referencias.json; usa `\cita` o `\citatexto` en LaTeX.
No edites las bibliografías generadas en .build/. Revisa el formato APA 7 según
el tipo de fuente: el script centraliza textos, no valida todas las reglas APA.
Ejecuta `python compilar.py --verificar` para validar el reporte. Usa
`python compilar.py --con-presentacion --verificar` para detectar diferencias de títulos,
expositores, cantidad de láminas o claves de citas antes de compilar.
Los apartados de tema, indicaciones y fuentes requieren interpretación y redacción;
no se convierten automáticamente en contenido académico.

Usa los datos y fuentes proporcionados. No inventes integrantes, códigos, nombres
de docentes, resultados ni referencias. Si falta información esencial, pregunta;
puedes avanzar con las partes independientes. En un borrador identifica lo pendiente.
Sustituye los textos de ejemplo cuando prepares un trabajo real y adapta las
secciones a la consigna. Cuando se solicite la presentación, mantén su coherencia
con el reporte; no actualices diapositivas por rutina al trabajar solo en el reporte.

Conserva ambos logos, sus proporciones y el azul institucional `#173864`.
Mantén diapositivas 16:9, textos breves y un pie con el expositor correspondiente.
No reduzcas indiscriminadamente el tamaño de letra para hacer caber contenido:
divide láminas o reorganiza la portada si hay muchos integrantes o títulos largos.
El reporte usa tamaño carta y firma tipográfica al final de todo su contenido,
incluidos los anexos. El texto de firma procede de `datos.md`; no agregar firma
a las diapositivas. Cuando prepares la presentación, asegúrate de reflejar los cambios
tanto en `presentacion.tex` como en `reveal.js/index.html`.

## Compilación y entrega obligatorias

Después de editar contenido o diseño, ejecuta `python3 compilar.py` desde la raíz
(en Windows, `python compilar.py`). El script descarga una versión fija de
Tectonic si falta en la carpeta de datos del usuario y la reutiliza en futuras
ramas y clones. No instales una copia por proyecto ni guardes el compilador en Git.
La primera ejecución y los paquetes nuevos necesitan red. Respeta los permisos
del entorno y solicita la autorización técnica necesaria si el sandbox bloquea
red o escritura fuera del repositorio; no eludas esas restricciones.

1. Compila el reporte con el script; incluye la presentación únicamente si fue solicitada.
2. Revisa `.build/reporte.log` y, si se compiló la presentación, `.build/presentacion.log`: resuelve referencias
   indefinidas, caracteres faltantes y desbordamientos visibles.
3. Inspecciona los PDF recién generados: logos completos, portada legible, tablas y pies sin cortes,
   numeración coherente y firma al final del reporte. Si hay herramientas de
   renderizado, guarda las capturas temporales en `.build/` o fuera del repositorio.
4. Entrega el reporte y un resumen breve de cambios y verificaciones. Solo si se
   solicitó la presentación, entrega también su PDF y el HTML web actualizados.

No declares la tarea terminada con PDF antiguos ni sustituyas LaTeX por una impresión PDF desde HTML.
Si la compilación queda bloqueada, explica el error y distingue los PDF anteriores de los nuevos. El script conserva los anteriores si uno falla.
`--sin-red` permite comprobar que el motor y los paquetes se reutilizan sin descargas.
El entregable predeterminado es `pdf/reporte.pdf`. Si se solicita la presentación,
se añaden `pdf/presentacion.pdf` y `reveal.js/index.html`. Conserva las fuentes
editables y los entregables anteriores no seleccionados. No hagas commit ni push salvo que se solicite.
