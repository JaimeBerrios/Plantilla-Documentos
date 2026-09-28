with open("reporte.tex", "r") as f:
    text = f.read()

refs = """
\\vspace{0.5cm}
\\begin{flushleft}
\\setlength{\\parindent}{-1.27cm}
\\setlength{\\leftskip}{1.27cm}

Chandramouli, R. (2022). \\textit{Guide to a secure enterprise network landscape} (NIST Special Publication 800-215). National Institute of Standards and Technology. \\url{https://doi.org/10.6028/NIST.SP.800-215}

Cybersecurity and Infrastructure Security Agency. (2022). \\textit{Layering network security through segmentation}. U.S. Department of Homeland Security. \\url{https://www.cisa.gov/sites/default/files/2023-01/layering-network-security-segmentation_infographic_508_0.pdf}

Hernández-Sampieri, R., \\& Mendoza Torres, C. P. (2023). \\textit{Metodología de la investigación: Las rutas cuantitativa, cualitativa y mixta} (2.ª ed.). McGraw Hill.

Instituto Internacional de Planeamiento de la Educación de la UNESCO. (s. f.). El Salvador: Perfil de educación. \\textit{Sistema de Información de Tendencias Educativas en América Latina (SITEAL)}. Recuperado el 27 de septiembre de 2026, de \\url{https://siteal.iiep.unesco.org/pais/el_salvador}

\\end{flushleft}
"""

start_marker = "\\section{Referencias bibliográficas}"
end_marker = "\\section{Cronograma}"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx + len(start_marker)] + refs + "\n" + text[end_idx:]
    with open("reporte.tex", "w") as f:
        f.write(new_text)
    print("Updated Refs")
else:
    print("Could not find markers")
