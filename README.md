# Plantilla de Presentaciones Beamer

Plantilla base para crear presentaciones académicas en LaTeX/Beamer. Está
pensada para clonar el repositorio, editar `presentacion.tex`, compilar desde
VS Code y obtener un PDF listo para exponer.

## Qué Incluye Esta Plantilla

- Una presentación Beamer editable en `presentacion.tex`.
- Un tema visual separado en `plantilla/unab_presentacion.sty`.
- Logos de portada dentro de `img/`.
- Compatibilidad con tildes y caracteres del español.
- Iconos Font Awesome 5 listos para usar en títulos, listas y bloques.
- Script de compilación para Windows en `compilar.ps1`.
- Configuración de VS Code para LaTeX Workshop.
- Página `index.html` en modo oscuro con cambio opcional a modo claro.
- PDF de referencia en `pdf/presentacion.pdf`.

## Checklist Rápido

Antes de editar una presentación, confirma esto:

- `pdflatex --version` funciona en PowerShell.
- VS Code tiene instalada la extensión `LaTeX Workshop`.
- El proyecto se abrió desde la carpeta raíz, donde está `presentacion.tex`.
- Los logos existen en `img/logo-unab.png` y `img/logo-facultad.png`.
- Los archivos están guardados como `UTF-8`.

## Qué Debes Instalar

### 1. Visual Studio Code

Descarga e instala VS Code:

```text
https://code.visualstudio.com/
```

### 2. Git

Git sirve para clonar el repositorio y versionar tus cambios:

```text
https://git-scm.com/downloads
```

Después de instalarlo, verifica en PowerShell:

```powershell
git --version
```

### 3. Una distribución LaTeX

Necesitas una distribución LaTeX para compilar `presentacion.tex` a PDF.

Opción recomendada en Windows:

```text
MiKTeX
https://miktex.org/download
```

Durante la instalación de MiKTeX:

- Instala para tu usuario o para todos los usuarios.
- Activa la instalación automática de paquetes cuando MiKTeX lo pregunte.
- Asegúrate de que MiKTeX agregue sus comandos al `PATH`.

Alternativa:

```text
TeX Live
https://www.tug.org/texlive/
```

Después de instalar MiKTeX o TeX Live, cierra y vuelve a abrir VS Code y
PowerShell. Luego verifica:

```powershell
pdflatex --version
```

Si ese comando funciona, ya puedes compilar.

### 4. Extensiones de VS Code

Instala estas extensiones desde la pestaña Extensions de VS Code:

- `LaTeX Workshop` de James Yu.
- `Spanish Language Pack for Visual Studio Code`, opcional.

Este repositorio incluye `.vscode/settings.json` con una receta lista para
compilar usando `compilar.ps1`.

## Cómo Usar La Plantilla Desde Cero

### 1. Clonar el repositorio

Abre PowerShell o la terminal de VS Code:

```powershell
git clone URL_DEL_REPOSITORIO mi-presentacion
cd mi-presentacion
code .
```

Si ya descargaste el proyecto como ZIP, descomprímelo y abre la carpeta en
VS Code con:

```powershell
code .
```

### 2. Abrir el archivo principal

En VS Code abre:

```text
presentacion.tex
```

Ese es el archivo que normalmente vas a editar.

### 3. Cambiar los datos de portada

Al inicio de `presentacion.tex` encontrarás esta zona:

```latex
\renewcommand{\TituloPresentacion}{TÍTULO DE LA\\PRESENTACIÓN}
\renewcommand{\SubtituloPresentacion}{Asignatura \textperiodcentered\ Facultad o carrera}
\renewcommand{\InstitucionPresentacion}{Nombre de la institución}
\renewcommand{\FacultadPresentacion}{Nombre de la facultad}
\renewcommand{\CatedraticoPresentacion}{Nombre del catedrático}
\renewcommand{\GrupoPresentacion}{Grupo}
\renewcommand{\LugarFechaPresentacion}{Lugar \textperiodcentered\ Fecha}
```

Cambia esos textos por los datos reales de tu exposición.

### 4. Cambiar integrantes

Edita este bloque:

```latex
\renewcommand{\IntegrantesPresentacion}{%
  \textcolor{unabblue}{\faUser} & Nombre & \texttt{Código} \\
  \textcolor{unabblue}{\faUser} & Nombre & \texttt{Código} \\
  \textcolor{unabblue}{\faUser} & Nombre & \texttt{Código} \\
}
```

Puedes agregar o quitar filas siguiendo la misma estructura.

### 5. Cambiar logos

Los logos están en:

```text
img/logo-unab.png
img/logo-facultad.png
```

Para usar otros logos, reemplaza esos archivos manteniendo los mismos nombres.
La portada los cargará automáticamente.

### 6. Agregar imágenes

Coloca tus imágenes dentro de `img/`.

Ejemplo:

```latex
\includegraphics[width=0.75\linewidth]{img/mi-imagen.png}
```

La lámina de reflexión busca opcionalmente:

```text
img/reflexion.png
```

Si ese archivo existe, se mostrará automáticamente.

### 7. Editar las láminas

Cada lámina tiene esta estructura general:

```latex
\expositor{Nombre}
\begin{frame}{\faInfoCircle \ Título de la lámina}
  Contenido de la lámina.
\end{frame}
```

El comando `\expositor{Nombre}` actualiza el pie de página con la persona que
expone esa lámina. Si no necesitas expositor individual, puedes usar:

```latex
\expositor{Grupo}
```

### 8. Dónde cambiar el diseño

Edita contenido en:

```text
presentacion.tex
```

Edita colores, portada, pie de página y estilo general en:

```text
plantilla/unab_presentacion.sty
```

Para uso normal, modifica solo `presentacion.tex`.

## Compilar Desde VS Code

### Método recomendado

1. Abre `presentacion.tex`.
2. Presiona `Ctrl + Shift + P`.
3. Busca `LaTeX Workshop: Build LaTeX project`.
4. Selecciona la receta:

```text
Compilar presentación seleccionada
```

El PDF final se genera en:

```text
pdf/presentacion.pdf
```

### Ver el PDF en VS Code

Con `presentacion.tex` abierto:

1. Presiona `Ctrl + Shift + P`.
2. Busca `LaTeX Workshop: View LaTeX PDF`.
3. El PDF se abrirá en una pestaña de VS Code.

Si no se abre, busca el archivo manualmente:

```text
pdf/presentacion.pdf
```

### Compilar desde terminal

También puedes compilar sin usar el botón de LaTeX Workshop:

```powershell
.\compilar.ps1
```

Si PowerShell bloquea scripts no firmados:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\compilar.ps1
```

Para compilar otro archivo `.tex`:

```powershell
.\compilar.ps1 -Archivo "presentacion.tex"
```

## Usar Tildes Y Español

Puedes escribir tildes directamente en `presentacion.tex`:

```text
á, é, í, ó, ú, ñ, ¿, ¡
```

La plantilla incluye:

```latex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish,es-noshorthands]{babel}
```

Guarda los archivos con codificación `UTF-8`. En VS Code puedes confirmarlo en
la barra inferior derecha, donde aparece la codificación del archivo.

## Usar Iconos Font Awesome

La plantilla carga `fontawesome5`, así que puedes usar iconos directamente en
títulos, listas, bloques y portada.

Ejemplo:

```latex
\begin{frame}{\faLightbulb \ Idea principal}
  \begin{itemize}
    \item \textbf{\faCheckCircle \ Punto clave:} descripción breve.
    \item \textbf{\faUsers \ Equipo:} descripción breve.
    \item \textbf{\faChartLine \ Resultado:} descripción breve.
  \end{itemize}
\end{frame}
```

Cambiar iconos de portada:

```latex
\renewcommand{\IconosPortada}{\faCloud \hspace{0.5cm} \faServer \hspace{0.5cm} \faNetworkWired}
```

Algunos iconos útiles:

```text
\faUser
\faUsers
\faLightbulb
\faInfoCircle
\faCheckCircle
\faBook
\faCloud
\faServer
\faNetworkWired
\faChartLine
\faBriefcase
\faTools
\faCogs
```

Si un icono no existe o no compila, cambia a otro nombre de icono o revisa que
MiKTeX haya instalado el paquete `fontawesome5`.

## Página De Vista Previa

El archivo `index.html` sirve como guía visual del proyecto. Puedes abrirlo
directamente en el navegador.

Incluye:

- Requisitos de instalación.
- Pasos para compilar desde VS Code.
- Flujo recomendado de trabajo.
- Explicación de tildes, logos e iconos.
- Errores comunes.
- Acceso al PDF generado.

El `index.html` inicia en modo oscuro y tiene un botón para cambiar a modo
claro. El efecto está inspirado en la View Transitions API usada por
`theme-toggle.rdsx.dev`. Si el navegador no soporta View Transitions, el cambio
de tema funciona sin animación.

Archivos relacionados:

```text
index.html
web/css/styles.css
web/js/app.js
```

## Estructura Del Proyecto

```text
presentacion.tex              Presentación principal editable
informacion_presentacion.md   Datos y guion base para reutilizar con IA
compilar.ps1                  Script de compilación

plantilla/
  unab_presentacion.sty       Tema visual Beamer institucional

img/
  logo-unab.png               Logo izquierdo
  logo-facultad.png           Logo derecho
  reflexion.png               Imagen opcional para la lámina de reflexión

pdf/
  presentacion.pdf            PDF generado

web/
  css/styles.css              Estilos de la página de vista previa
  js/app.js                   Datos de ayuda para la página
  preview.html                Vista previa imprimible para generar PDF sin LaTeX

.vscode/
  settings.json               Configuración de LaTeX Workshop
  extensions.json             Extensiones recomendadas
```

## Errores Comunes

### `pdflatex` no se reconoce

Significa que MiKTeX o TeX Live no está instalado, o no está agregado al `PATH`.

Solución:

1. Instala MiKTeX o TeX Live.
2. Cierra VS Code.
3. Cierra PowerShell.
4. Abre VS Code de nuevo.
5. Ejecuta:

```powershell
pdflatex --version
```

### Falta un paquete LaTeX

Si MiKTeX pregunta si deseas instalar un paquete faltante, acepta la instalación.
Esta plantilla usa paquetes como Beamer, TikZ y FontAwesome 5.

### PowerShell bloquea `compilar.ps1`

Usa:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\compilar.ps1
```

La receta de VS Code ya usa esa opción automáticamente.

### Los acentos se ven mal

Verifica que el archivo esté guardado como `UTF-8` en VS Code.

También confirma que `presentacion.tex` tenga:

```latex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish,es-noshorthands]{babel}
```

### Los iconos no compilan

Verifica que el paquete `fontawesome5` esté instalado. Si usas MiKTeX, permite
la instalación automática cuando aparezca el aviso.

### No se actualiza el PDF

Revisa que estés compilando el archivo correcto:

```text
presentacion.tex
```

También confirma que el PDF generado esté en:

```text
pdf/presentacion.pdf
```

### El visor de VS Code muestra un PDF viejo

Cierra la pestaña del PDF y vuelve a ejecutar:

```text
LaTeX Workshop: View LaTeX PDF
```

También puedes abrir el PDF directamente desde la carpeta `pdf/`.

## Qué Archivo Debo Tocar

| Necesidad | Archivo |
|---|---|
| Cambiar título, integrantes y contenido | `presentacion.tex` |
| Cambiar colores, pie de página o portada | `plantilla/unab_presentacion.sty` |
| Cambiar logos | `img/logo-unab.png` y `img/logo-facultad.png` |
| Agregar imágenes | `img/` |
| Compilar manualmente | `compilar.ps1` |
| Configurar VS Code | `.vscode/settings.json` |
| Leer datos base para IA | `informacion_presentacion.md` |
| Ver guía visual | `index.html` |

## Flujo Recomendado Para Cada Nueva Presentación

1. Clona o copia esta plantilla.
2. Reemplaza los logos en `img/` si es necesario.
3. Edita los datos iniciales de `presentacion.tex`.
4. Cambia el contenido de cada lámina.
5. Compila desde VS Code con LaTeX Workshop.
6. Revisa `pdf/presentacion.pdf`.
7. Guarda o sube tus cambios a Git.
