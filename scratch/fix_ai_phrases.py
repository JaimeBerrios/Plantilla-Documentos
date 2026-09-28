import re

with open("reporte.tex", "r") as f:
    text = f.read()

replacements = [
    (r"debido a que se pretende establecer controles", "puesto que el propósito es establecer controles"),
    (r"debido a que permiten controlar", "ya que facilitan el control de"),
    (r"debido a que su funcionamiento puede afectar", "considerando que cualquier fallo en su funcionamiento afecta directamente"),
    (r"debido a que corresponde a la configuración utilizada", "al coincidir con la configuración actualmente instalada"),
    (r"debido a que la infraestructura tecnológica", "entendiendo que la infraestructura tecnológica"),
    (r"debido a que el funcionamiento de servicios", "dado que la provisión de servicios"),
    (r"debido a que las variables no serán manipuladas", "ya que no habrá manipulación de variables"),
    (r"debido a que se recopilarán y analizarán datos", "al basarse en la recopilación y el análisis de datos"),
    (r"debido a que no se modificarán deliberadamente", "por el hecho de que no se alterarán deliberadamente"),
    (r"debido a que la recopilación de información se realizará", "en vista de que los datos se recolectarán"),
]

for old, new in replacements:
    text = re.sub(old, new, text)

# Alcance
old_alcance = "Desde el componente descriptivo, se caracterizará la infraestructura de red existente, su topología, los dispositivos utilizados, la distribución de la conectividad y las principales condiciones que pueden representar riesgos para la seguridad informática.\n\nDesde el componente propositivo, se diseñará un modelo de seguridad perimetral y segmentación lógica que permita establecer una arquitectura de red más segura."
new_alcance = "Su fase descriptiva consistirá en caracterizar la topología, los dispositivos, la distribución de conectividad y los posibles factores de riesgo en la infraestructura actual. Sobre esta base, su dimensión propositiva abarcará el diseño de un modelo de seguridad perimetral y segmentación lógica para conformar una arquitectura sólidamente protegida."

text = text.replace(old_alcance, new_alcance)

with open("reporte.tex", "w") as f:
    f.write(text)

print("Applied replacements")
