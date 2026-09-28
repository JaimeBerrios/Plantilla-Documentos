with open("reporte.tex", "r") as f:
    text = f.read()

with open("scratch/replacement.tex", "r") as f:
    replacement = f.read()

start_marker = "\\section{Marco teórico}"
end_marker = "\\section{Análisis e interpretación de los resultados}"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx] + replacement + "\n\n" + text[end_idx:]
    with open("reporte.tex", "w") as f:
        f.write(new_text)
    print("Updated")
else:
    print("Markers not found")

