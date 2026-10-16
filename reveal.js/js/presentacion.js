// Usa data-expositor="Nombre" en cada lámina; "grupo" toma el valor de datos.md.
function actualizarPie(event) {
  const slide = event.currentSlide;
  const nombre = slide.dataset.expositor || "";
  document.querySelector(".pie").hidden = !nombre;
  document.querySelector("#expositor").textContent = nombre === "grupo"
    ? document.querySelector('[data-campo="Grupo"]').textContent
    : nombre;
}

Reveal.on("ready", actualizarPie);
Reveal.on("slidechanged", actualizarPie);
Reveal.initialize({
  width: 1280,
  height: 720,
  margin: 0.04,
  hash: true,
  slideNumber: "c/t",
  plugins: [RevealNotes]
});
