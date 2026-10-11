with open("reporte.tex", "r") as f:
    text = f.read()

old_table = """\\begin{table}[h]
    \\centering
    \\footnotesize
    \\begin{tabularx}{\\textwidth}{|>{\\raggedright\\arraybackslash}p{2.2cm}|>{\\raggedright\\arraybackslash}X|>{\\raggedright\\arraybackslash}X|c|c|c|}
    \\hline
    \\textbf{Activo} & \\textbf{Amenaza} & \\textbf{Vulnerabilidad} & \\textbf{Probabilidad} & \\textbf{Impacto} & \\textbf{Riesgo} \\\\
    \\hline
    \\textbf{Switch Central} (Topología física) & Falla de hardware e interrupción masiva del servicio & Alto grado de obsolescencia (instalado aprox. en 2003) y puertos físicos dañados. & Alta & Alto & \\textbf{Crítico} \\\\
    \\hline
    \\textbf{Equipos Administrativos} & Movimiento lateral de \\textit{malware} o accesos no autorizados & Operación en una red plana (dominio de \\textit{broadcast} único) sin segmentación VLAN. & Alta & Alto & \\textbf{Crítico} \\\\
    \\hline
    \\textbf{Equipos en Diagnóstico} & Infección por conexión de dispositivos externos comprometidos & Ausencia de una red o DMZ aislada para soporte técnico. & Media & Alto & \\textbf{Alto} \\\\
    \\hline
    \\textbf{Tráfico Saliente} & Acceso a sitios maliciosos o consumo indebido de red & Desincorporación del servidor central y del proxy SQUID para filtrado perimetral. & Alta & Medio & \\textbf{Alto} \\\\
    \\hline
    \\textbf{Conexiones Inalámbricas} & Interceptación de datos no encriptados (ataque MITM) & Tránsito de datos sin políticas forzadas de encriptación (HTTPS/TLS). & Media & Medio & \\textbf{Medio} \\\\
    \\hline
    \\end{tabularx}
    \\vspace{0.2cm}
    \\caption{Matriz de análisis y evaluación de riesgos de la infraestructura actual.}
    \\label{tab:matriz_riesgos}
\\end{table}"""

new_table = """\\begin{table}[h]
    \\centering
    \\footnotesize
    \\renewcommand{\\arraystretch}{1.5} % Dar un respiro vertical al texto
    \\begin{tabularx}{\\textwidth}{@{} >{\\raggedright\\arraybackslash}p{2.5cm} >{\\raggedright\\arraybackslash}X >{\\raggedright\\arraybackslash}X c c c @{}}
    \\toprule
    \\textbf{\\color{unabblue}Activo} & \\textbf{\\color{unabblue}Amenaza} & \\textbf{\\color{unabblue}Vulnerabilidad} & \\textbf{\\color{unabblue}Probabilidad} & \\textbf{\\color{unabblue}Impacto} & \\textbf{\\color{unabblue}Riesgo} \\\\
    \\midrule
    \\textbf{Switch Central}\\newline(Topología física) & Falla de hardware e interrupción masiva del servicio & Alto grado de obsolescencia (instalado aprox. en 2003) y puertos físicos dañados. & Alta & Alto & \\textbf{Crítico} \\\\
    \\textbf{Equipos}\\newline\\textbf{Administrativos} & Movimiento lateral de \\textit{malware} o accesos no autorizados & Operación en una red plana (dominio de \\textit{broadcast} único) sin segmentación VLAN. & Alta & Alto & \\textbf{Crítico} \\\\
    \\textbf{Equipos en}\\newline\\textbf{Diagnóstico} & Infección por conexión de dispositivos externos comprometidos & Ausencia de una red o DMZ aislada para soporte técnico. & Media & Alto & \\textbf{Alto} \\\\
    \\textbf{Tráfico Saliente} & Acceso a sitios maliciosos o consumo indebido de red & Desincorporación del servidor central y del proxy SQUID para filtrado perimetral. & Alta & Medio & \\textbf{Alto} \\\\
    \\textbf{Conexiones}\\newline\\textbf{Inalámbricas} & Interceptación de datos no encriptados (ataque MITM) & Tránsito de datos sin políticas forzadas de encriptación (HTTPS/TLS). & Media & Medio & \\textbf{Medio} \\\\
    \\bottomrule
    \\end{tabularx}
    \\vspace{0.1cm}
    \\caption{Matriz de análisis y evaluación de riesgos de la infraestructura actual.}
    \\label{tab:matriz_riesgos}
\\end{table}"""

text = text.replace(old_table, new_table)

with open("reporte.tex", "w") as f:
    f.write(text)

print("Table beautified")
