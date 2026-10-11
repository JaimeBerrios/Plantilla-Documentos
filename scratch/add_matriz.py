with open("reporte.tex", "r") as f:
    text = f.read()

matriz_text = """\\subsection{Matriz de Análisis y Evaluación de Riesgos}

Como parte de la fase de gestión de riesgos, se procedió a categorizar los hallazgos técnicos identificados en la sede mediante una matriz estructurada. Esta matriz permite priorizar las vulnerabilidades según la probabilidad de ocurrencia y el impacto que tendrían sobre la triada CIA (Confidencialidad, Integridad y Disponibilidad) de la información institucional.

\\begin{table}[h]
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
\\end{table}

La evaluación confirma que las debilidades más críticas se concentran en la falta de segmentación lógica y en la obsolescencia del hardware central. Estos niveles de riesgo justifican plenamente la urgencia de desplegar el modelo propuesto, utilizando un esquema de VLANs, listas de control de acceso (ACLs) y filtrado perimetral.

"""

end_idx = text.find("\\section{Conclusiones}")

if end_idx != -1:
    new_text = text[:end_idx] + matriz_text + text[end_idx:]
    with open("reporte.tex", "w") as f:
        f.write(new_text)
    print("Injected Matriz de Riesgos")
else:
    print("Could not find Conclusiones section")
