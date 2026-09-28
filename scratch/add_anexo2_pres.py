with open("presentacion.tex", "r") as f:
    text = f.read()

new_frame = """
\\begin{frame}{Anexos: Reunión de trabajo (Fase 2)}
  \\begin{figure}
    \\centering
    \\includegraphics[height=0.7\\textheight,keepaspectratio]{assets/img/anexos/reunion-2/foto-1.jpeg}
    \\caption{Desarrollo del Marco Teórico y Metodología.}
  \\end{figure}
\\end{frame}
"""

text = text.replace("\\end{document}", new_frame + "\n\\end{document}")

with open("presentacion.tex", "w") as f:
    f.write(text)

print("Added Frame 2")
