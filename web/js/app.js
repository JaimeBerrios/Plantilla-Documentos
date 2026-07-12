const installs = [
  ["VS Code", "Editor", "Instala Visual Studio Code para editar y compilar desde LaTeX Workshop."],
  ["Git", "Control de versiones", "Permite clonar el repositorio y guardar cambios."],
  ["MiKTeX o TeX Live", "Motor LaTeX", "Incluye pdflatex y los paquetes necesarios para generar el PDF."],
  ["LaTeX Workshop", "Extensión", "Agrega comandos de compilación, visor PDF y diagnósticos en VS Code."]
];

const files = [
  ["presentacion.tex", "Contenido", "Datos generales, portada y láminas de la exposición."],
  ["plantilla/unab_presentacion.sty", "Tema visual", "Colores, portada, pie de página, bloques e iconos Font Awesome."],
  ["informacion_presentacion.md", "Briefing", "Fuente base para pedirle a una IA que actualice la presentación."],
  ["img/", "Recursos", "Logos, imágenes de apoyo y material gráfico de cada exposición."],
  [".vscode/settings.json", "VS Code", "Receta lista para compilar con LaTeX Workshop."],
  ["compilar.ps1", "Compilación", "Genera el PDF final dentro de la carpeta pdf/."]
];

const workflow = [
  ["1", "Copia o clona", "Crea una carpeta nueva para cada presentación y abre el proyecto en VS Code."],
  ["2", "Reemplaza logos", "Cambia `img/logo-unab.png` y `img/logo-facultad.png` si usarás otra identidad."],
  ["3", "Edita datos", "Actualiza título, asignatura, catedrático, grupo, fecha e integrantes."],
  ["4", "Escribe láminas", "Sustituye los textos de ejemplo y agrega imágenes dentro de `img/`."],
  ["5", "Compila", "Usa LaTeX Workshop o ejecuta `.\compilar.ps1` desde PowerShell."],
  ["6", "Revisa PDF", "Abre `pdf/presentacion.pdf` y corrige texto, espaciado o imágenes."]
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
