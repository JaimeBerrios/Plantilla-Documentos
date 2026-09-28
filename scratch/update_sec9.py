with open("reporte.tex", "r") as f:
    text = f.read()

with open("scratch/sec9.txt", "r") as f:
    sec9_text = f.read().replace("9. ANÁLISIS E INTERPRETACIÓN DE LOS RESULTADOS \n\n", "")

start_marker = "\\section{Análisis e interpretación de los resultados}"
end_marker = "\\section{Conclusiones}"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx + len(start_marker)] + "\n\n" + sec9_text + "\n" + text[end_idx:]
    with open("reporte.tex", "w") as f:
        f.write(new_text)
    print("Updated Section 9")
else:
    print("Could not find markers")
