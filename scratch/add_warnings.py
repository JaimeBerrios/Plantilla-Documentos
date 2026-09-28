import re

with open("reporte.tex", "r") as f:
    text = f.read()

warning_start = "\n% ==============================================================================\n% ¡ATENCIÓN! ESTIPULACIÓN IMPORTANTE DEL USUARIO:\n% POR NINGÚN MOTIVO SE DEBE MODIFICAR LA PORTADA, TÍTULO, PLANTEAMIENTO DEL PROBLEMA,\n% JUSTIFICACIÓN, NI LOS OBJETIVOS DE LA INVESTIGACIÓN. ESTAS SECCIONES SON DEFINITIVAS.\n% ==============================================================================\n"

warning_end = "\n% ==============================================================================\n% FIN DE SECCIONES PROTEGIDAS Y DEFINITIVAS\n% ==============================================================================\n"

# find where "Título de la investigación" starts
t_idx = text.find("\\section{Título de la investigación}")

# find where "Marco teórico" starts
m_idx = text.find("\\section{Marco teórico}")

if t_idx != -1 and m_idx != -1:
    new_text = text[:t_idx] + warning_start + text[t_idx:m_idx] + warning_end + text[m_idx:]
    with open("reporte.tex", "w") as f:
        f.write(new_text)
    print("Added warnings to reporte.tex")
else:
    print("Could not find sections")
