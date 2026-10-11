with open("reporte.tex", "r") as f:
    text = f.read()

old_obj = """\\subsection{Objetivos específicos}
% \\begin{itemize}
  % \\item Diagnosticar las condiciones técnicas actuales de la infraestructura,
  estaciones y flujos de tráfico, identificando vulnerabilidades y amenazas.
  % \\item Formular una matriz de análisis y evaluación de riesgos y Políticas de
  Seguridad Informática alineadas al marco regulatorio y operativo institucional.
  % \\item Estructurar en GNS3 una arquitectura perimetral con VLAN, ACL y
  cortafuegos Linux para aislar zonas administrativas, técnicas y de diagnóstico.
  % \\item Configurar controles de capa de aplicación mediante proxy y certificados
  digitales HTTPS/TLS en un laboratorio simulado.
% \\end{itemize}"""

new_obj = """\\subsection{Objetivos específicos}
\\begin{itemize}
  \\item Diagnosticar las condiciones técnicas actuales de la infraestructura,
  estaciones y flujos de tráfico, identificando vulnerabilidades y amenazas.
  \\item Formular una matriz de análisis y evaluación de riesgos y Políticas de
  Seguridad Informática alineadas al marco regulatorio y operativo institucional.
  \\item Estructurar en GNS3 una arquitectura perimetral con VLAN, ACL y
  cortafuegos Linux para aislar zonas administrativas, técnicas y de diagnóstico.
  \\item Configurar controles de capa de aplicación mediante proxy y certificados
  digitales HTTPS/TLS en un laboratorio simulado.
\\end{itemize}"""

text = text.replace(old_obj, new_obj)

with open("reporte.tex", "w") as f:
    f.write(text)

print("Fixed objectives")
