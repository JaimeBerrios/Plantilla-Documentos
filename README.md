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

   > Lee AGENTS.md y datos.md. Prepara únicamente el reporte para este trabajo,
   > conserva la identidad de la universidad y mi firma. Compila y revisa el PDF.

   Pide expresamente la presentación cuando también necesites sus versiones PDF y web.

5. Abre **[reporte PDF](pdf/reporte.pdf)**. Si pediste la presentación, abre también
   **[presentación PDF](pdf/presentacion.pdf)** y **[presentación web](reveal.js/index.html)**.
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
compilación** (`Ctrl+Shift+B`), que genera **solo el reporte**.

Para incluir explícitamente la presentación PDF y actualizar el HTML:

```bash
python compilar.py --con-presentacion
```

En VS Code elige la tarea **Generar reporte y presentación (PDF y web)**.
Sin esta opción, no se leen ni validan las fuentes de las diapositivas y no se
modifican `pdf/presentacion.pdf` ni `reveal.js/index.html`; sus versiones existentes
pueden corresponder a un trabajo anterior. `--sin-red` se puede combinar con ambos modos.

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
al reporte; con `--con-presentacion`, también a las diapositivas PDF y web.
La firma solo se usa en el reporte.
El resto del archivo es una guía para Codex: compilar no
redacta ni investiga el contenido por sí solo.

Solo cuando todos los documentos seleccionados compilan correctamente se actualizan
sus PDF en `pdf/`. Si hay un error, el comando termina con error y conserva las versiones
anteriores; revisa los registros en `.build/` antes de entregar el trabajo.
El HTML solo se actualiza con `--con-presentacion`, después de que ambos PDF compilan.

## Archivos que se conservan

```text
datos.md                         Datos y consigna del trabajo
presentacion.tex                 Contenido de las diapositivas
reporte.tex                      Contenido del documento
compilar.py                      Compilación PDF y sincronización de datos web
AGENTS.md                        Instrucciones para Codex
README.md                        Esta guía
plantilla/                       Dos estilos institucionales reutilizables
assets/img/institucional/        Logos, variantes y acreditación
assets/img/contenido/            Imágenes y gráficos del trabajo
assets/fonts/firma.otf           Fuente original de la firma
pdf/                             Presentación y reporte listos para abrir
reveal.js/index.html             Contenido editable de las diapositivas web
reveal.js/css/unab.css           Diseño institucional de las diapositivas web
reveal.js/js/presentacion.js     Configuración 16:9 y pies de expositores
vendor/reveal.js/                Biblioteca local, versión y licencia
index.html                      Guía web y acceso a los tres entregables
web/                            CSS y JavaScript de la guía web
.editorconfig                   Codificación UTF-8 y formato de texto
.vscode/tasks.json               Compilación desde VS Code
```

Edita normalmente `datos.md` y `reporte.tex`. Prepara las diapositivas solo cuando
las necesites expresamente. Puedes
agregar imágenes de apoyo en `assets/img/contenido/`. Los dos logos siempre se conservan.
La firma toma el texto del campo `Firma` y solo aparece al final del reporte.

`.build/` contiene datos generados y registros; está excluida de Git. Los PDF sí
se versionan, para que cada rama conserve sus entregables. No se necesita
GitHub Actions ni una distribución LaTeX completa instalada manualmente.

## Presentación web y guía

Abre `index.html` para consultar la guía, o `reveal.js/index.html` para exponer.
La presentación usa recursos locales y se puede abrir sin conexión; la guía
utiliza Bootstrap y Font Awesome desde CDN y necesita conexión para esos estilos.
Conserva `vendor/`, `assets/` y `reveal.js/` juntos cuando compartas la versión web.

Los elementos `<span data-campo="…">` y `<tbody id="integrantes">` son zonas de
sincronización de `compilar.py`. Edita sus valores en `datos.md`; los cambios
manuales dentro de esas zonas se reemplazan al compilar con `--con-presentacion`. El resto del HTML es
editable y el script lo conserva. La firma no se incorpora al HTML.

El contenido académico de las láminas se mantiene manualmente en
`presentacion.tex` y `reveal.js/index.html`: la compilación sincroniza datos,
no convierte LaTeX en HTML. En el HTML, `data-expositor="Nombre"` define el pie
de cada lámina; `data-expositor="grupo"` usa el grupo de `datos.md`.
En LaTeX, usa `\expositor{Nombre}`. Si hay muchos integrantes o títulos largos,
divide o reorganiza las láminas en ambas versiones y revisa su presentación.

El diseño web propio vive en `reveal.js/css/` y `reveal.js/js/`; no modifiques
`vendor/` para personalizarlo. La versión de la biblioteca está documentada en
`vendor/reveal.js/README.md`. Los ejemplos de la biblioteca no son entregables.

## Verificación del compilador

`python compilar.py --verificar` valida datos y citas del reporte sin compilar.
Con `python compilar.py --con-presentacion --verificar` también se comprueban
cantidad, orden, títulos, expositores y claves de citas de las diapositivas.
Ninguno de estos comandos modifica entregables. La compilación ejecuta las
comprobaciones del modo seleccionado y se detiene si encuentra errores.

Se admiten las macros institucionales de portada/cierre y láminas
`\begin{frame}{Título}` con texto simple e iconos `\faNombre`. El HTML usa
secciones planas con un `h1` o `h2` por lámina. Títulos con macros complejas o
secciones anidadas producen un error explícito; no se interpretan silenciosamente.
Esta comprobación compara la estructura de las fuentes, no su significado ni
el número de páginas adicionales que pudieran producir overlays de Beamer.

## Referencias compartidas: APA 7

Edita `referencias.json`. Cada entrada incluye:

- `id`: clave estable para citar, por ejemplo `fuente`.
- `orden`: clave alfabética de autor y, cuando proceda, fecha y título.
- `autor_parentetico`: autores tal como aparecen dentro de paréntesis.
- `autor_narrativo`: autores tal como aparecen dentro de la oración.
- `anio`: año, o `s. f.`; incluye `a`/`b` cuando sea necesario desambiguar.
- `referencia`: referencia completa redactada en APA 7; delimita cursivas con
  `*texto*`. Admite texto normal, DOI y URL, sin comandos LaTeX ni HTML.
- `ejemplo`: `true` para ejemplos didácticos; cámbialo a `false` al aportar una
  fuente real y comprobar sus datos.

En ambos `.tex`, usa `\cita{fuente}` para `(Apellido, Año)` y
`\citatexto{fuente}` para `Apellido (Año)`. Para citas textuales, incluye el
localizador: `\cita[p. 10]{fuente}`. La cita no agrega comillas ni transforma
el texto citado en una cita en bloque: redacta esos elementos según la consigna.
En el HTML usa `<span data-cita="fuente"></span>` y, si corresponde,
`data-tipo="narrativa"` y `data-localizador="p. 10"` en el mismo elemento.
Los atributos de sincronización usan comillas dobles.

El compilador genera `.build/citas.tex` y la bibliografía del reporte.
Solo con `--con-presentacion` genera además la bibliografía de las diapositivas
y actualiza el bloque `referencias:inicio` / `referencias:fin` del HTML.
No edites esas salidas. Cada documento incluye solo sus fuentes citadas;
la presentación PDF y web deben citar el mismo conjunto de claves.
El reporte usa sangría francesa de 1.27 cm y doble espacio en las referencias.

Este mecanismo **centraliza referencias redactadas en APA 7**, no convierte
metadatos incompletos a APA ni valida automáticamente todas sus reglas.
Revisa autores, fechas, puntuación, cursivas, DOI y desambiguación según el tipo
de fuente. En particular, configura correctamente `&`, `y` y `et al.` en los
dos campos de autor. Usa los [ejemplos oficiales APA](https://apastyle.apa.org/style-grammar-guidelines/references/examples)
y las [reglas de citas](https://apastyle.apa.org/style-grammar-guidelines/citations).
El ejemplo inicial es ficticio y está marcado como tal; no es una fuente real.
Si una bibliografía extensa no cabe en una lámina, reorganiza ambas versiones
y adapta los bloques de generación antes de entregar; no reduzcas la letra.

## Pruebas

Ejecuta `python -m unittest discover -s tests` para comprobar el escape de datos
y la conservación del contenido HTML, además de la coherencia y las citas. Después ejecuta `python compilar.py` y
revisa el reporte. Prueba el modo de presentación explícito cuando corresponda.

Referencias técnicas: [Tectonic](https://tectonic-typesetting.github.io/en-US/install.html)
y [las instrucciones AGENTS.md de Codex](https://developers.openai.com/codex/guides/agents-md).
