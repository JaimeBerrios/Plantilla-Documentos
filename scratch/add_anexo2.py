with open("reporte.tex", "r") as f:
    text = f.read()

new_figure = """
\\begin{figure}[h]
    \\centering
    \\includegraphics[width=0.8\\textwidth]{assets/img/anexos/reunion-2/foto-1.jpeg}
    \\caption{Reunión de trabajo para el desarrollo del Marco Teórico, Metodología y Análisis de Resultados.}
    \\label{fig:anexo2}
\\end{figure}
"""

# Insert before \end{document}
text = text.replace("\\end{document}", new_figure + "\n\\end{document}")

with open("reporte.tex", "w") as f:
    f.write(text)

print("Added Figure 2")
