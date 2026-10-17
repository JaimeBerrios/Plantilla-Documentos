# Organización del repositorio

| Carpeta | Qué contiene |
|---|---|
| `datos/` | Única fuente de metadatos, integrantes, consigna y bibliografía. |
| `documentos/` | Contenido LaTeX, fragmentos y anexos editables. |
| `plantilla/latex/` | Estilos reutilizables; no guardar contenido de un trabajo aquí. |
| `web/portal/` | CSS y JavaScript del portal de la raíz. |
| `web/presentacion/` | Diapositivas HTML, tema, estilos propios e interacciones. |
| `assets/institucional/` | Logos y acreditación originales; conservar proporciones. |
| `assets/fuentes/` | Fuentes locales, incluida la firma original. |
| `assets/iconos/fontawesome/` | SVG oficiales y licencia de la selección de iconos. |
| `assets/contenido/` | Imágenes, gráficos y evidencias del trabajo. |
| `herramientas/` | Implementación Python; `compilar.py` sigue siendo la entrada única. |
| `vendor/` | Reveal.js, Bootstrap y Font Awesome locales con versión y licencia, sin personalizaciones. |
| `ejemplos/` | Demos que no forman parte de la entrega académica. |
| `docs/` | Guías de mantenimiento y uso. |
| `pdf/` | Entregables PDF generados y versionados. |
| `tests/` | Comprobaciones automatizadas. |
| `.build/` | Datos, referencias, registros y capturas temporales; fuera de Git. |

El portal `index.html` permanece en la raíz. Su presentación está en
`web/presentacion/index.html`; no hay otra copia editable en `reveal.js/`.

Las rutas de LaTeX se resuelven desde `documentos/`: usa `../assets/`,
`../plantilla/latex/` y `../.build/`. El compilador fija la raíz del repositorio
para sus datos y salidas, aunque se invoque desde otro directorio.
Las rutas HTML y CSS se resuelven desde el archivo que las contiene.

Para añadir una sección extensa usa `\input{secciones/nombre.tex}` desde el documento.
No dupliques archivos para conservar rutas antiguas: actualiza sus consumidores y pruebas.
