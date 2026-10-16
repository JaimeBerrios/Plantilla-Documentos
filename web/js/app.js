const installs = [
  ["Python 3.9+", "Requerido", "Ejecuta compilar.py sin paquetes adicionales de pip."],
  ["Tectonic", "Automático", "El script descarga la versión fija y la reutiliza fuera del repositorio."],
  ["VS Code", "Opcional", "Edita los archivos y compila con Ctrl + Shift + B."],
  ["Git", "Versiones", "Conserva fuentes y entregables en una rama por trabajo."]
];
const files = [
  ["referencias.json", "APA 7", "Referencias y formas de cita compartidas; el texto bibliográfico se redacta según el tipo de fuente."],
  ["python compilar.py --con-presentacion --verificar", "Coherencia", "Comprueba cantidad, títulos, expositores y claves de citas entre las presentaciones sin compilar."],
  ["datos.md", "Datos y consigna", "Datos generales e integrantes compartidos por los PDF y la presentación web."],
  ["presentacion.tex y reporte.tex", "Contenido", "Textos académicos editables de los dos documentos."],
  ["reveal.js/index.html", "Diapositivas web", "Contenido editable; mantén su correspondencia con presentacion.tex."],
  ["plantilla/", "Diseño LaTeX", "Estilos institucionales reutilizables de presentación y reporte."],
  ["assets/img/", "Recursos", "institucional/ contiene los logos; contenido/ las imágenes del trabajo."],
  ["compilar.py", "Compilación", "Genera solo el reporte. Añade --con-presentacion para incluir las diapositivas PDF y web."],
  ["vendor/reveal.js/", "Dependencia", "Biblioteca local con versión y licencia; no editar para cambiar el diseño."],
  ["reveal.js/css/ y reveal.js/js/", "Diseño web", "Tema institucional y configuración de las diapositivas."]
];
const workflow = [
  ["1", "Prepara tu rama", "Guarda el trabajo anterior y crea una rama descriptiva para el nuevo proyecto."],
  ["2", "Completa los datos", "Edita datos.md con integrantes, asignatura, consigna y fuentes."],
  ["3", "Redacta el trabajo", "Actualiza reporte.tex. Prepara las diapositivas solo si también necesitas una presentación."],
  ["4", "Agrega imágenes", "Guarda el material del trabajo en assets/img/contenido/. Conserva los logos institucionales."],
  ["5", "Compila", "Ejecuta python compilar.py desde la raíz; en Linux y macOS usa python3."],
  ["6", "Revisa los entregables", "Comprueba el reporte y, si solicitaste la presentación, revisa también sus versiones PDF y web."]
];

function renderCards(container, items) {
  container.innerHTML = items.map(([title, label, description]) => `
    <div class="col-md-6">
      <article class="info-card">
        <span>${label}</span>
        <h3>${title}</h3>
        <p>${description}</p>
      </article>
    </div>
  `).join("");
}

renderCards(document.querySelector("#installGrid"), installs);
renderCards(document.querySelector("#fileGrid"), files);
renderCards(document.querySelector("#workflowGrid"), workflow);

document.querySelector("#currentYear").textContent = new Date().getFullYear();

const root = document.documentElement;
const themeToggle = document.querySelector("#themeToggle");
const themeIcon = themeToggle.querySelector("i");

function applyTheme(theme) {
  const dark = theme === "dark";
  root.classList.toggle("dark", dark);
  root.classList.toggle("light", !dark);
  root.dataset.theme = theme;
  themeToggle.setAttribute("aria-label", dark ? "Cambiar a modo claro" : "Cambiar a modo oscuro");
  themeIcon.className = dark ? "fa-solid fa-moon" : "fa-solid fa-sun";
  localStorage.setItem("theme", theme);
}

function switchTheme() {
  applyTheme(root.classList.contains("dark") ? "light" : "dark");
}

applyTheme(localStorage.getItem("theme") || "dark");

themeToggle.addEventListener("click", () => {
  if (!document.startViewTransition) {
    switchTheme();
    return;
  }

  document.startViewTransition(switchTheme);
});
