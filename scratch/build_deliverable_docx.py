import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def build_advance_docx():
    doc = docx.Document('info/borrador.docx')

    # Update Objective 4 if present
    for p in doc.paragraphs:
        if 'Implementar controles de capa de aplicación' in p.text:
            p.text = p.text.replace('Implementar controles de capa de aplicación', 'Configurar controles de capa de aplicación mediante proxy y certificados digitales HTTPS/TLS en un laboratorio simulado')
        if '30 de septiembre de 2026' in p.text:
            p.text = p.text.replace('30 de septiembre de 2026', '12 de octubre de 2026')

    # Find the end of Section 9
    sec9_end_idx = None
    for i, p in enumerate(doc.paragraphs):
        if 'En síntesis, los resultados obtenidos sirven como base' in p.text:
            sec9_end_idx = i
            break

    # Add Risk Matrix table to section 9
    doc.add_paragraph()
    p_mat = doc.add_paragraph()
    r_mat = p_mat.add_run("Tabla 1: Matriz de Análisis y Evaluación de Riesgos (Fase 2)")
    r_mat.bold = True
    r_mat.font.color.rgb = RGBColor(0x17, 0x38, 0x64)
    r_mat.font.name = 'Arial'

    p_desc = doc.add_paragraph("A continuación se presenta la matriz de riesgos formal elaborada para la infraestructura tecnológica de la sede:")
    p_desc.runs[0].font.name = 'Arial'

    # Create table: 6 columns, 6 rows
    headers = ["Activo", "Amenaza", "Vulnerabilidad", "Probabilidad", "Impacto", "Nivel de Riesgo"]
    rows_data = [
        ("Switch central de distribución", "Fallo físico total o interrupción", "Obsolescencia tecnológica (operativo desde 2003)", "Alta", "Crítico", "Extremo"),
        ("Estaciones de trabajo técnico/admin", "Infección y propagación lateral de malware", "Arquitectura de red plana sin segmentación ni VLAN", "Alta", "Alto", "Alto"),
        ("Puntos de acceso Wi-Fi", "Acceso no autorizado a la red institucional", "Falta de aislamiento para redes de invitados y personal", "Media", "Alto", "Medio"),
        ("Equipos externos en diagnóstico", "Contaminación cruzada de estaciones", "Conexión directa en el mismo dominio de difusión", "Alta", "Crítico", "Extremo"),
        ("Tráfico de salida a Internet (ISP)", "Fuga de información y consumo desmedido", "Ausencia de servidor proxy y filtrado de contenido", "Media", "Medio", "Medio")
    ]

    table = doc.add_table(rows=len(rows_data) + 1, cols=6)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Format header row
    hdr_cells = table.rows[0].cells
    for col_idx, header_text in enumerate(headers):
        cell = hdr_cells[col_idx]
        cell.text = header_text
        set_cell_background(cell, "173864")
        set_cell_margins(cell, top=120, bottom=120, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.font.bold = True
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            run.font.size = Pt(9.5)
            run.font.name = 'Arial'

    # Fill data rows
    for row_idx, row_values in enumerate(rows_data):
        row_cells = table.rows[row_idx + 1].cells
        bg_color = "F9FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, val in enumerate(row_values):
            cell = row_cells[col_idx]
            cell.text = val
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=100, bottom=100, left=80, right=80)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx >= 3 else WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.name = 'Arial'
                run.font.size = Pt(9)
                if col_idx == 5:
                    run.font.bold = True
                    if val == "Extremo":
                        run.font.color.rgb = RGBColor(0xB0, 0x00, 0x20)
                    elif val == "Alto":
                        run.font.color.rgb = RGBColor(0xE6, 0x51, 0x00)
                    else:
                        run.font.color.rgb = RGBColor(0xFB, 0x8C, 0x00)

    doc.add_paragraph()

    # Section 10 & 11 placeholders
    p10 = doc.add_paragraph()
    r10 = p10.add_run("10. CONCLUSIONES")
    r10.bold = True
    r10.font.color.rgb = RGBColor(0x17, 0x38, 0x64)
    r10.font.name = 'Arial'
    doc.add_paragraph("(Apartado correspondiente a la Fase 4 de la investigación acumulativa de cátedra.)")

    p11 = doc.add_paragraph()
    r11 = p11.add_run("11. RECOMENDACIONES")
    r11.bold = True
    r11.font.color.rgb = RGBColor(0x17, 0x38, 0x64)
    r11.font.name = 'Arial'
    doc.add_paragraph("(Apartado correspondiente a la Fase 4 de la investigación acumulativa de cátedra.)")

    # Section 12: Referencias
    p12 = doc.add_paragraph()
    r12 = p12.add_run("12. REFERENCIAS BIBLIOGRÁFICAS")
    r12.bold = True
    r12.font.color.rgb = RGBColor(0x17, 0x38, 0x64)
    r12.font.name = 'Arial'

    refs = [
        "Cybersecurity and Infrastructure Security Agency. (s. f.). Layering network security through segmentation. CISA. Recuperado el 27 de septiembre de 2026, de https://www.cisa.gov/news-events/news/layering-network-security-through-segmentation",
        "Hernández-Sampieri, R., y Mendoza Torres, C. P. (2023). Metodología de la investigación: Las rutas cuantitativa, cualitativa y mixta (2.ª ed.). McGraw-Hill.",
        "Instituto Internacional de Planeamiento de la Educación de la UNESCO. (s. f.). El Salvador: Perfil de educación. Sistema de Información de Tendencias Educativas en América Latina (SITEAL). Recuperado el 27 de septiembre de 2026, de https://siteal.iiep.unesco.org/pais/el_salvador",
        "National Institute of Standards and Technology. (2020). Guide to a Secure Enterprise Network Architecture (NIST Special Publication 800-215). U.S. Department of Commerce."
    ]
    for ref in refs:
        p_ref = doc.add_paragraph(ref)
        p_ref.paragraph_format.left_indent = Inches(0.5)
        p_ref.paragraph_format.first_line_indent = Inches(-0.5)
        for r in p_ref.runs:
            r.font.name = 'Arial'
            r.font.size = Pt(10)

    # Section 15: Anexos
    doc.add_paragraph()
    p15 = doc.add_paragraph()
    r15 = p15.add_run("15. ANEXOS")
    r15.bold = True
    r15.font.color.rgb = RGBColor(0x17, 0x38, 0x64)
    r15.font.name = 'Arial'

    # Annex 1
    p_anx1 = doc.add_paragraph("Anexo 1: Sesión de lectura y análisis del protocolo institucional")
    p_anx1.runs[0].bold = True
    p_anx1.runs[0].font.name = 'Arial'
    if os.path.exists("assets/img/anexos/reunion-1/horizontal-1.jpeg"):
        doc.add_picture("assets/img/anexos/reunion-1/horizontal-1.jpeg", width=Inches(5.5))
    doc.add_paragraph("Figura 1. Revisión de requisitos y delimitación metodológica por el equipo investigador.")

    # Annex 2
    p_anx2 = doc.add_paragraph("Anexo 2: Sesión de formulación metodológica y matriz de riesgos (Fase 2)")
    p_anx2.runs[0].bold = True
    p_anx2.runs[0].font.name = 'Arial'
    if os.path.exists("assets/img/anexos/reunion-2/foto-2.jpeg"):
        doc.add_picture("assets/img/anexos/reunion-2/foto-2.jpeg", width=Inches(5.5))
    doc.add_paragraph("Figura 2. Desarrollo del Marco Teórico, Metodología y Matriz de Riesgos.")

    out_path = '2026_II_SeguridadPerimetral_y_AseguramientoRedDatos/Documento_de_Avance_Fase2.docx'
    doc.save(out_path)
    print(f"Generado exitosamente: {out_path}")

if __name__ == '__main__':
    build_advance_docx()
