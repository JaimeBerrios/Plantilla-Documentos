import os
import re
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

UNAB_BLUE = RGBColor(0x17, 0x38, 0x64)
HEX_UNAB_BLUE = "173864"
TEXT_COLOR = RGBColor(0x22, 0x22, 0x22)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="173864", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideH w:val="none"/>'
        f'  <w:insideV w:val="none"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def set_row_bottom_border(row, color="173864", sz="4"):
    for cell in row.cells:
        tcPr = cell._tc.get_or_add_tcPr()
        tcBorders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}><w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/></w:tcBorders>'
        )
        tcPr.append(tcBorders)

def add_styled_paragraph(doc, text="", style='Normal', space_before=0, space_after=6, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, bold=False, italic=False, font_size=11, color=TEXT_COLOR):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    if text:
        run = p.add_run(text)
        run.bold = bold
        run.italic = italic
        run.font.name = 'Arial'
        run.font.size = Pt(font_size)
        run.font.color.rgb = color
    return p

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.bold = True
    run.font.name = 'Arial'
    run.font.size = Pt(14)
    run.font.color.rgb = UNAB_BLUE
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.bold = True
    run.font.name = 'Arial'
    run.font.size = Pt(12)
    run.font.color.rgb = UNAB_BLUE
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.bold = True
    run.font.name = 'Arial'
    run.font.size = Pt(11)
    run.font.color.rgb = UNAB_BLUE
    return p

def add_bullet_item(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.left_indent = Inches(0.5)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = 'Arial'
        r_pre.font.size = Pt(11)
        r_pre.font.color.rgb = TEXT_COLOR
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(11)
    run.font.color.rgb = TEXT_COLOR
    return p

def create_document():
    doc = docx.Document()

    # Set margins to 2.54 cm (1 inch)
    section = doc.sections[0]
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    section.page_width = Inches(8.5)
    section.page_height = Inches(11.0)

    # Configure different first page for cover
    section.different_first_page_header_footer = True

    # Header for regular pages
    header = section.header
    p_head = header.paragraphs[0]
    p_head.text = ""

    # Footer for regular pages
    footer = section.footer
    p_foot = footer.paragraphs[0]
    p_foot.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_f1 = p_foot.add_run("Diseño de Sistemas de Seguridad de Redes de Datos")
    r_f1.font.name = 'Arial'
    r_f1.font.size = Pt(8.5)
    r_f1.font.color.rgb = UNAB_BLUE

    # =========================================================================
    # PORTADA (PÁGINA 1)
    # =========================================================================
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_before = Pt(10)
    p_logo.paragraph_format.space_after = Pt(12)
    if os.path.exists("assets/img/logo-portada.png"):
        p_logo.add_run().add_picture("assets/img/logo-portada.png", width=Inches(1.6))

    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.line_spacing = 1.15
    p_inst.paragraph_format.space_after = Pt(2)
    r_inst = p_inst.add_run("UNIVERSIDAD DR. ANDRÉS BELLO")
    r_inst.bold = True
    r_inst.font.name = 'Arial'
    r_inst.font.size = Pt(14)
    r_inst.font.color.rgb = UNAB_BLUE

    p_sede = doc.add_paragraph()
    p_sede.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sede.paragraph_format.line_spacing = 1.15
    p_sede.paragraph_format.space_after = Pt(2)
    r_sede = p_sede.add_run("Sede Regional de San Miguel\nFacultad de Tecnología e Innovación\nIngeniería en Sistemas y Computación")
    r_sede.font.name = 'Arial'
    r_sede.font.size = Pt(11)
    r_sede.font.color.rgb = TEXT_COLOR

    # Espacio vertical
    p_sp1 = doc.add_paragraph()
    p_sp1.paragraph_format.space_before = Pt(16)
    p_sp1.paragraph_format.space_after = Pt(4)
    p_sp1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_lbl = p_sp1.add_run("TEMA DE INVESTIGACIÓN")
    r_lbl.font.name = 'Arial'
    r_lbl.font.size = Pt(10)
    r_lbl.font.color.rgb = UNAB_BLUE

    p_tema = doc.add_paragraph()
    p_tema.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_tema.paragraph_format.line_spacing = 1.15
    p_tema.paragraph_format.space_after = Pt(8)
    r_tema = p_tema.add_run("Diseño de un modelo de seguridad perimetral y segmentación lógica para el aseguramiento de la red de datos en la Sede de Enlaces con la Educación, Distrito de Santa Rosa de Lima, Municipio de La Unión Norte, El Salvador, 2026.")
    r_tema.bold = True
    r_tema.font.name = 'Arial'
    r_tema.font.size = Pt(14)
    r_tema.font.color.rgb = UNAB_BLUE

    # Línea divisoria
    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line.paragraph_format.space_after = Pt(16)
    r_line = p_line.add_run("—" * 28)
    r_line.font.color.rgb = UNAB_BLUE
    r_line.bold = True

    # Asignatura y Docente
    p_asig = doc.add_paragraph()
    p_asig.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_asig.paragraph_format.line_spacing = 1.15
    p_asig.paragraph_format.space_after = Pt(14)
    r_asig = p_asig.add_run("Asignatura: ")
    r_asig.bold = True
    r_asig.font.name = 'Arial'
    r_asig.font.size = Pt(10.5)
    r_asig2 = p_asig.add_run("Diseño de Sistemas de Seguridad de Redes de Datos\n")
    r_asig2.font.name = 'Arial'
    r_asig2.font.size = Pt(10.5)

    r_doc = p_asig.add_run("Docente: ")
    r_doc.bold = True
    r_doc.font.name = 'Arial'
    r_doc.font.size = Pt(10.5)
    r_doc2 = p_asig.add_run("MduEV. Ing. Franklin Geovany Buruca Hernández")
    r_doc2.font.name = 'Arial'
    r_doc2.font.size = Pt(10.5)

    # Integrantes header
    p_integ = doc.add_paragraph()
    p_integ.paragraph_format.space_after = Pt(4)
    r_integ = p_integ.add_run("Integrantes")
    r_integ.bold = True
    r_integ.font.name = 'Arial'
    r_integ.font.size = Pt(10.5)

    # Integrantes table (Estilo booktabs idéntico a LaTeX: líneas superior/inferior sobrias, sin sombreados de IA)
    tbl_int = doc.add_table(rows=6, cols=2)
    tbl_int.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_int, color="000000", sz="4", val="single")

    int_data = [
        ("Nombre completo", "Código"),
        ("Genesis Abigail Saravia Carpio", "sc0139042023"),
        ("Jaime Fernando Berrios Ortiz", "bo0310042024"),
        ("Jefferson Jared Bonilla Meléndez", "bm0749042022"),
        ("Rosmeri Estefani González Pérez", "gp0382042023"),
        ("Florentín Alexander Treminio Herrera", "th0988042023")
    ]

    for r_idx, (nom, cod) in enumerate(int_data):
        c0, c1 = tbl_int.rows[r_idx].cells
        c0.text = nom
        c1.text = cod
        c1.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        set_cell_margins(c0, top=30, bottom=30, left=40, right=40)
        set_cell_margins(c1, top=30, bottom=30, left=40, right=40)
        for c in (c0, c1):
            p = c.paragraphs[0]
            if r_idx == 0:
                p.runs[0].bold = True
                p.runs[0].font.color.rgb = RGBColor(0, 0, 0)
            p.runs[0].font.name = 'Arial'
            p.runs[0].font.size = Pt(10)

    set_row_bottom_border(tbl_int.rows[0], color="000000", sz="4")

    p_fecha = doc.add_paragraph()
    p_fecha.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_fecha.paragraph_format.space_before = Pt(20)
    r_fecha = p_fecha.add_run("San Miguel, 12 de octubre de 2026")
    r_fecha.font.name = 'Arial'
    r_fecha.font.size = Pt(10)
    r_fecha.font.color.rgb = TEXT_COLOR

    doc.add_page_break()

    # =========================================================================
    # ÍNDICE GENERAL (PÁGINA 2)
    # =========================================================================
    add_heading_1(doc, "Índice general")
    p_toc_desc = add_styled_paragraph(doc, "Contenido del documento de investigación:", space_after=10)

    toc_items = [
        ("2. Título de la investigación", "1"),
        ("3. Introducción", "1"),
        ("4. Planteamiento del problema", "1"),
        ("    4.1 Situación problemática", "1"),
        ("    4.2 Enunciado del problema", "1"),
        ("5. Justificación", "1"),
        ("6. Objetivos de la investigación", "2"),
        ("    6.1 Objetivo general", "2"),
        ("    6.2 Objetivos específicos", "2"),
        ("7. Marco teórico", "2"),
        ("    7.1 Seguridad informática", "3"),
        ("    7.2 Seguridad de redes", "3"),
        ("    7.3 Seguridad perimetral", "3"),
        ("    7.4 Segmentación lógica de redes", "4"),
        ("    7.5 Listas de control de acceso (ACL)", "5"),
        ("    7.6 Cortafuegos y filtrado del tráfico", "5"),
        ("    7.7 Proxy y control de acceso a servicios de Internet", "6"),
        ("    7.8 HTTPS/TLS y protección de las comunicaciones", "6"),
        ("    7.9 Topologías de red", "7"),
        ("    7.10 Infraestructura actual de la Sede de Enlaces con la Educación", "7"),
        ("    7.11 Marco normativo y planificación educativa en El Salvador", "8"),
        ("        7.11.1 Compromisos y obligaciones jurídicas en el ámbito nacional", "8"),
        ("        7.11.2 Planificación de la educación", "8"),
        ("        7.11.3 Caracterización de la política educativa nacional", "9"),
        ("    7.12 Relación de los fundamentos teóricos con el modelo propuesto", "9"),
        ("8. Metodología", "10"),
        ("    8.1 Tipo y diseño de investigación", "10"),
        ("    8.2 Unidad de análisis", "10"),
        ("    8.3 Caracterización de la infraestructura actual", "10"),
        ("    8.4 Problemática de seguridad informática", "11"),
        ("    8.5 Técnicas e instrumentos para la recopilación de información", "11"),
        ("    8.6 Propuesta tecnológica", "11"),
        ("9. Análisis e interpretación de los resultados", "12"),
        ("    9.1 Matriz de Análisis y Evaluación de Riesgos", "12"),
        ("10. Conclusiones", "14"),
        ("11. Recomendaciones", "14"),
        ("12. Referencias bibliográficas", "14"),
        ("13. Cronograma", "15"),
        ("14. Presupuesto", "15"),
        ("15. Anexos", "15")
    ]

    tbl_toc = doc.add_table(rows=len(toc_items), cols=2)
    tbl_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_toc, color="FFFFFF", sz="0", val="none")

    for i, (item_text, pg) in enumerate(toc_items):
        c0, c1 = tbl_toc.rows[i].cells
        c0.text = item_text
        c1.text = pg
        c1.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        set_cell_margins(c0, top=10, bottom=10, left=30, right=30)
        set_cell_margins(c1, top=10, bottom=10, left=30, right=30)
        p0 = c0.paragraphs[0]
        p1 = c1.paragraphs[0]
        p0.paragraph_format.line_spacing = 1.15
        p1.paragraph_format.line_spacing = 1.15
        p0.paragraph_format.space_after = Pt(1.5)
        p1.paragraph_format.space_after = Pt(1.5)
        for r in (p0.runs[0], p1.runs[0]):
            r.font.name = 'Arial'
            r.font.size = Pt(9.5)
            if not item_text.startswith("    "):
                r.bold = True
                r.font.color.rgb = UNAB_BLUE
            else:
                r.font.color.rgb = TEXT_COLOR

    # Crear una nueva sección para el cuerpo del documento, reiniciando la numeración en 1 (igual que en LaTeX)
    sec_body = doc.add_section(docx.enum.section.WD_SECTION_START.NEW_PAGE)
    sec_body.top_margin = Inches(1.0)
    sec_body.bottom_margin = Inches(1.0)
    sec_body.left_margin = Inches(1.0)
    sec_body.right_margin = Inches(1.0)
    sec_body.page_width = Inches(8.5)
    sec_body.page_height = Inches(11.0)
    sec_body.different_first_page_header_footer = False

    # Reiniciar numeración de páginas en 1
    sectPr = sec_body._sectPr
    pgNumType = parse_xml(r'<w:pgNumType %s w:start="1"/>' % nsdecls('w'))
    sectPr.append(pgNumType)

    # Header de la sección del cuerpo
    sec_body.header.is_linked_to_previous = False
    sec_body.header.paragraphs[0].text = ""

    # Footer de la sección del cuerpo
    sec_body.footer.is_linked_to_previous = False
    p_foot_b = sec_body.footer.paragraphs[0]
    p_foot_b.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_f_lbl = p_foot_b.add_run("Diseño de Sistemas de Seguridad de Redes de Datos           Página ")
    r_f_lbl.font.name = 'Arial'
    r_f_lbl.font.size = Pt(8.5)
    r_f_lbl.font.color.rgb = UNAB_BLUE

    # Campo de página dinámica en Word
    fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
    fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    t_val = parse_xml(r'<w:t %s>1</w:t>' % nsdecls('w'))
    r_val = parse_xml(r'<w:r %s/>' % nsdecls('w'))
    r_val.append(t_val)
    fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))

    r1 = parse_xml(r'<w:r %s/>' % nsdecls('w'))
    r1.append(fldChar1)
    r2 = parse_xml(r'<w:r %s/>' % nsdecls('w'))
    r2.append(instrText)
    r3 = parse_xml(r'<w:r %s/>' % nsdecls('w'))
    r3.append(fldChar2)
    r4 = parse_xml(r'<w:r %s/>' % nsdecls('w'))
    r4.append(fldChar3)

    p_foot_b._p.append(r1)
    p_foot_b._p.append(r2)
    p_foot_b._p.append(r3)
    p_foot_b._p.append(r_val)
    p_foot_b._p.append(r4)

    # =========================================================================
    # CONTENIDO DEL DOCUMENTO
    # =========================================================================

    # 1. TÍTULO
    add_heading_1(doc, "2. Título de la investigación")
    add_styled_paragraph(doc, "Diseño de un modelo de seguridad perimetral y segmentación lógica para el aseguramiento de la red de datos en la Sede de Enlaces con la Educación, Distrito de Santa Rosa de Lima, Municipio de La Unión Norte, El Salvador, 2026.")

    # 2. INTRODUCCIÓN
    add_heading_1(doc, "3. Introducción")

    # 3. PLANTEAMIENTO DEL PROBLEMA
    add_heading_1(doc, "4. Planteamiento del problema")
    add_heading_2(doc, "4.1 Situación problemática")
    add_styled_paragraph(doc, "Las sedes de soporte técnico e infraestructura digital del sector educativo manejan volúmenes significativos de tráfico y equipos con diferentes niveles de confianza. En la sede interactúan estaciones del personal de planta con laptops y tabletas estudiantiles que ingresan para mantenimiento. La arquitectura actual es predominantemente plana y no existe una separación lógica formal entre los dominios técnico y administrativo. Equipos en revisión, potencialmente desactualizados o infectados con malware, comparten el canal con sistemas que procesan registros institucionales.")
    add_styled_paragraph(doc, "La red carece de ACL estrictas, inspección de estado mediante cortafuegos dedicados, NAT estructurado por zonas y filtrado en capa de aplicación. Tampoco se dispone de políticas formales para el uso seguro de puertos y servicios. Esta carencia eleva la probabilidad de denegación de servicio interna, fugas de información, accesos no autorizados e interrupciones en la entrega de equipos.")

    add_heading_2(doc, "4.2 Enunciado del problema")
    add_styled_paragraph(doc, "¿De qué manera el diseño de un modelo de seguridad perimetral y segmentación lógica contribuirá a mitigar los riesgos informáticos y garantizar la confidencialidad, integridad y disponibilidad en la red de datos de la Sede de Enlaces con la Educación en Santa Rosa de Lima durante 2026?")

    # 4. JUSTIFICACIÓN
    add_heading_1(doc, "5. Justificación")
    add_styled_paragraph(doc, "La investigación responde a la necesidad de dotar a la sede de un esquema de seguridad formal, preventivo y técnicamente viable. La propuesta aborda las vulnerabilidades estructurales mediante VLAN para aislar dispositivos en diagnóstico, estaciones administrativas y servidores locales; reglas de filtrado perimetral en Linux; y servicios proxy para auditar el tráfico y optimizar el ancho de banda. En el ámbito académico y profesional, permite aplicar competencias de seguridad de redes, gestión de riesgos, simulación en GNS3 y normativa informática salvadoreña. El resultado esperado es una base documental replicable en otras sedes regionales.")

    # 5. OBJETIVOS
    add_heading_1(doc, "6. Objetivos de la investigación")
    add_heading_2(doc, "6.1 Objetivo general")
    add_styled_paragraph(doc, "Diseñar un modelo de seguridad perimetral y segmentación lógica para la red de datos de la Sede de Enlaces con la Educación en el distrito de Santa Rosa de Lima, con el fin de mitigar riesgos informáticos y preservar la confidencialidad, integridad y disponibilidad del tráfico institucional durante 2026.")

    add_heading_2(doc, "6.2 Objetivos específicos")
    add_bullet_item(doc, "Diagnosticar las condiciones técnicas actuales de la infraestructura, estaciones y flujos de tráfico, identificando vulnerabilidades y amenazas.")
    add_bullet_item(doc, "Formular una matriz de análisis y evaluación de riesgos y Políticas de Seguridad Informática alineadas al marco regulatorio y operativo institucional.")
    add_bullet_item(doc, "Estructurar en GNS3 una arquitectura perimetral con VLAN, ACL y cortafuegos Linux para aislar zonas administrativas, técnicas y de diagnóstico.")
    add_bullet_item(doc, "Configurar controles de capa de aplicación mediante proxy y certificados digitales HTTPS/TLS en un laboratorio simulado.")

    # 6. MARCO TEÓRICO
    add_heading_1(doc, "7. Marco teórico")
    add_styled_paragraph(doc, "Diseñar una infraestructura de red resiliente exige articular los principios de seguridad de la información con las técnicas de conmutación y filtrado de paquetes. En la Sede de Enlaces con la Educación (distrito de Santa Rosa de Lima), este marco cobra relevancia directa ante la presencia de una topología centralizada en estrella que concentra el tráfico de diez puestos técnicos sin barreras de aislamiento interno.")

    add_heading_2(doc, "7.1 Seguridad informática")
    add_styled_paragraph(doc, "La seguridad informática engloba las políticas, controles técnicos y procedimientos destinados a salvaguardar los activos digitales y la infraestructura de comunicaciones frente a incidentes intencionados o accidentales.")
    add_styled_paragraph(doc, "Su marco operativo gravita sobre la tríada CIA: confidencialidad (acceso restringido a entidades legítimas), integridad (preservación de la exactitud de los datos frente a alteraciones no autorizadas) y disponibilidad (acceso continuo a los servicios cuando la labor institucional lo requiera). En redes locales compartidas, vulnerar cualquiera de estos pilares impacta directamente en las operaciones diarias. Por ello, la protección efectiva trasciende la simple instalación de software: exige clasificar activos, dimensionar vectores de amenaza y mitigar vulnerabilidades mediante controles técnicos proporcionados.")

    add_heading_2(doc, "7.2 Seguridad de redes")
    add_styled_paragraph(doc, "La seguridad de redes constituye una aplicación de los principios de seguridad informática orientada específicamente a proteger la infraestructura de comunicaciones, los dispositivos conectados y el tráfico que circula entre ellos. Su finalidad es establecer mecanismos que permitan controlar las comunicaciones y reducir la posibilidad de accesos o intercambios de información no autorizados.")
    add_styled_paragraph(doc, "La protección de una red puede implementarse mediante diferentes controles, entre ellos cortafuegos, listas de control de acceso, segmentación de red, autenticación, monitoreo del tráfico y establecimiento de políticas para determinar qué dispositivos pueden comunicarse entre sí.")
    add_styled_paragraph(doc, "La seguridad de redes adquiere especial importancia cuando dispositivos con funciones o niveles de confianza diferentes utilizan una misma infraestructura. Una red sin separación suficiente entre grupos de dispositivos puede incrementar la exposición de los recursos ante incidentes originados en otro equipo conectado.")
    add_styled_paragraph(doc, "En este sentido, organismos especializados en ciberseguridad recomiendan implementar segmentación mediante mecanismos como VLAN, listas de control de acceso en routers y capacidades de firewall como parte de una estrategia de defensa en profundidad.")

    add_heading_2(doc, "7.3 Seguridad perimetral")
    add_styled_paragraph(doc, "La seguridad perimetral comprende los mecanismos destinados a controlar las comunicaciones entre diferentes zonas de una red y entre la infraestructura interna y redes externas. El perímetro representa un punto de control desde el cual pueden establecerse reglas para permitir, restringir, inspeccionar o registrar las comunicaciones.")
    add_styled_paragraph(doc, "Uno de los principales componentes utilizados para establecer este control es el firewall o cortafuegos. Este dispositivo o software analiza el tráfico de red de acuerdo con reglas previamente establecidas y determina qué comunicaciones se permiten o se bloquean. Dependiendo de su implementación, puede realizar inspección del tráfico considerando direcciones IP, puertos, protocolos, conexiones y otros parámetros.")
    add_styled_paragraph(doc, "El diseño de un perímetro de seguridad no debe entenderse exclusivamente como una barrera entre Internet y la red interna. En arquitecturas segmentadas también pueden establecerse controles entre diferentes zonas internas, de manera que el acceso de un segmento a otro se encuentre sujeto a políticas específicas.")
    add_styled_paragraph(doc, "Para la presente investigación, este concepto constituye uno de los fundamentos de la arquitectura propuesta, puesto que el propósito es establecer controles que permitan regular el tráfico entre los diferentes grupos de dispositivos que forman parte de la infraestructura de la sede.")

    add_heading_2(doc, "7.4 Segmentación lógica de redes")
    add_styled_paragraph(doc, "La segmentación de redes consiste en dividir una infraestructura en diferentes segmentos con el propósito de establecer límites de comunicación y facilitar la aplicación de políticas de seguridad. Esta separación puede realizarse físicamente mediante equipos independientes o lógicamente mediante tecnologías de red.")
    add_styled_paragraph(doc, "CISA define la segmentación como una aproximación arquitectónica física o virtual mediante la cual una red es dividida en múltiples segmentos que funcionan como subredes independientes, proporcionando mayor control sobre las comunicaciones.")
    add_styled_paragraph(doc, "Una de las tecnologías empleadas para realizar esta separación lógica son las Virtual Local Area Networks (VLAN). Las VLAN permiten agrupar dispositivos lógicamente aunque utilicen una infraestructura física común. De esta manera, los equipos pueden organizarse de acuerdo con su función, nivel de confianza o requerimientos de seguridad.")
    add_styled_paragraph(doc, "NIST señala que, en un enfoque tradicional de segmentación, los recursos que poseen requerimientos de seguridad similares pueden agruparse en segmentos mediante mecanismos como identificadores VLAN, mientras las políticas de comunicación se establecen utilizando parámetros de red como direcciones IP y puertos.")
    add_styled_paragraph(doc, "La utilización de VLAN permite disminuir la comunicación directa e innecesaria entre grupos de dispositivos. Sin embargo, la segmentación por sí sola no constituye un mecanismo completo de protección; debe complementarse con reglas que determinen qué tráfico puede circular entre los diferentes segmentos.")

    add_heading_2(doc, "7.5 Listas de control de acceso (ACL)")
    add_styled_paragraph(doc, "Las listas de control de acceso, conocidas como ACL por sus siglas en inglés (Access Control Lists), permiten establecer reglas para autorizar o denegar determinados tipos de tráfico de red.")
    add_styled_paragraph(doc, "Las ACL pueden utilizar criterios como direcciones IP de origen y destino, protocolos y puertos para determinar si una comunicación debe permitirse. De esta manera, permiten aplicar restricciones entre diferentes segmentos de una infraestructura.")
    add_styled_paragraph(doc, "En una arquitectura segmentada, las ACL complementan el uso de VLAN ya que facilitan el control de la comunicación entre ellas. Esto posibilita establecer, por ejemplo, que un determinado segmento tenga acceso únicamente a los servicios necesarios para desarrollar sus funciones, evitando comunicaciones que no hayan sido expresamente autorizadas.")
    add_styled_paragraph(doc, "La aplicación de estos controles responde al principio de reducir las comunicaciones innecesarias entre grupos de dispositivos. CISA incluye las ACL de router junto con los firewalls y las VLAN entre los mecanismos que pueden utilizarse para conseguir una segmentación robusta de la red.")

    add_heading_2(doc, "7.6 Cortafuegos y filtrado del tráfico")
    add_styled_paragraph(doc, "Un firewall constituye un mecanismo de seguridad encargado de controlar el tráfico que atraviesa diferentes interfaces o zonas de una red. Su funcionamiento se basa en políticas y reglas mediante las cuales se determina qué comunicaciones pueden establecerse y cuáles deben ser rechazadas.")
    add_styled_paragraph(doc, "Los cortafuegos pueden utilizarse tanto para controlar las conexiones procedentes de redes externas como para establecer restricciones entre segmentos internos. En una arquitectura de seguridad por capas, estos controles permiten crear fronteras entre recursos que presentan diferentes niveles de confianza.")
    add_styled_paragraph(doc, "CISA señala que los firewalls pueden configurarse para bloquear tráfico proveniente de determinadas direcciones de red, aplicaciones o puertos, permitiendo simultáneamente las comunicaciones que resultan necesarias para el funcionamiento de los servicios.")
    add_styled_paragraph(doc, "Para el modelo propuesto en esta investigación se considera el empleo de un cortafuegos basado en Linux dentro del ambiente simulado, con el propósito de establecer reglas de filtrado y controlar las comunicaciones entre los segmentos definidos.")

    add_heading_2(doc, "7.7 Proxy y control de acceso a servicios de Internet")
    add_styled_paragraph(doc, "Un servidor proxy funciona como intermediario entre los dispositivos de una red y determinados servicios externos. Las solicitudes realizadas por los usuarios pueden ser procesadas por el proxy antes de establecer comunicación con el recurso solicitado.")
    add_styled_paragraph(doc, "Su implementación puede utilizarse para establecer políticas de navegación, controlar determinados tipos de solicitudes, mantener registros de actividad y aplicar restricciones de acceso de acuerdo con las necesidades de una organización.")
    add_styled_paragraph(doc, "Este elemento posee además un antecedente directo dentro de la infraestructura objeto de estudio. De acuerdo con la información proporcionada por la sede, anteriormente existía un servidor central encargado de filtrar y distribuir el acceso a Internet y se utilizaba un proxy físico para realizar funciones de filtrado. Con modificaciones realizadas posteriormente a la infraestructura, tanto el servidor como el proxy dejaron de utilizarse, permaneciendo principalmente el switch y el cableado de la red.")
    add_styled_paragraph(doc, "Por tanto, estudiar la función del proxy permite comprender tanto parte de la arquitectura que existió anteriormente como las posibilidades de incorporar controles de capa de aplicación dentro del modelo propuesto.")

    add_heading_2(doc, "7.8 HTTPS/TLS y protección de las comunicaciones")
    add_styled_paragraph(doc, "La seguridad de una red no solamente requiere controlar qué dispositivos pueden establecer comunicación, sino también proteger la información mientras es transmitida. Para ello pueden utilizarse protocolos criptográficos destinados a proporcionar seguridad a las comunicaciones.")
    add_styled_paragraph(doc, "Transport Layer Security (TLS) permite establecer comunicaciones protegidas mediante mecanismos criptográficos. Su utilización está asociada, entre otras aplicaciones, con HTTPS, mediante el cual se protege la comunicación entre clientes y servicios web.")
    add_styled_paragraph(doc, "Los certificados digitales forman parte de este proceso al permitir vincular una identidad con información criptográfica utilizada durante el establecimiento de comunicaciones seguras. La incorporación de HTTPS/TLS en un ambiente de laboratorio permite analizar mecanismos destinados a proteger la información durante su transmisión y complementar los controles de segmentación y filtrado establecidos en la arquitectura.")

    add_heading_2(doc, "7.9 Topologías de red")
    add_styled_paragraph(doc, "Una topología de red representa la forma en que los diferentes dispositivos y medios de comunicación se encuentran organizados dentro de una infraestructura. Entre las topologías conocidas se encuentran bus, anillo, malla, árbol y estrella.")
    add_styled_paragraph(doc, "En una topología estrella, los dispositivos se conectan hacia un punto central encargado de concentrar las conexiones. Esta configuración facilita la administración de los enlaces, aunque también genera una dependencia significativa respecto del dispositivo central, considerando que cualquier fallo en su funcionamiento afecta directamente la conectividad de los equipos asociados.")
    add_styled_paragraph(doc, "La topología estrella resulta particularmente relevante para la presente investigación al coincidir con la configuración actualmente instalada en la Sede de Enlaces con la Educación. Según la información proporcionada por la institución, la red ha mantenido esta topología desde su implementación y actualmente las conexiones se concentran principalmente en un switch.")

    add_heading_2(doc, "7.10 Infraestructura actual de la Sede de Enlaces con la Educación")
    add_styled_paragraph(doc, "La Sede de Enlaces con la Educación del distrito de Santa Rosa de Lima dispone actualmente de una infraestructura en la que los dispositivos utilizados por el personal comparten una misma red. De acuerdo con la información proporcionada por la sede, se encuentran diez equipos de oficina, correspondientes a los técnicos que trabajan en la institución.")
    add_styled_paragraph(doc, "La infraestructura utiliza una topología estrella cuyo punto de concentración es un switch. Este equipo se encuentra instalado desde aproximadamente el año 2003 y actualmente presenta diferentes puertos que han dejado de funcionar. La sede indica que algunos puertos permanecen operativos, pero el dispositivo presenta deterioro debido a su antigüedad.")
    add_styled_paragraph(doc, "La arquitectura original disponía de un servidor central encargado del filtrado y distribución de Internet y de un proxy físico. Tras remodelaciones estructurales en el inmueble, ambos equipos quedaron fuera de servicio, conservándose únicamente el cableado y el switch central. En el esquema actual, la conectividad se reparte entre bocas cableadas y routers inalámbricos secundarios.")
    add_styled_paragraph(doc, "En cuanto al enlace externo, la sede opera con un módem provisto por la compañía de telecomunicaciones. Debido al daño en varios puntos de pared, la computadora de la administración se conecta de forma directa a una de las tres salidas físicas del módem, compartiendo dicho acceso con el sistema de videovigilancia y un router adicional.")
    add_styled_paragraph(doc, "Estas condiciones fundamentan la necesidad de diseñar una arquitectura con segmentación lógica y barreras perimetrales, derivando las vulnerabilidades concretas del diagnóstico técnico de campo.")

    add_heading_2(doc, "7.11 Marco normativo y planificación educativa en El Salvador")
    add_styled_paragraph(doc, "La infraestructura tecnológica objeto de estudio se encuentra dentro de un contexto educativo y, por tanto, resulta pertinente considerar el marco jurídico y de planificación que orienta el sistema educativo salvadoreño.")
    add_styled_paragraph(doc, "El Sistema de Información de Tendencias Educativas en América Latina (SITEAL), del Instituto Internacional de Planeamiento de la Educación de UNESCO, establece que los compromisos nacionales relacionados con el derecho a la educación se encuentran expresados principalmente mediante la Constitución y las leyes nacionales de educación. Para El Salvador, identifica a la Constitución de la República como el marco de mayor jerarquía para la protección del derecho a la educación y a la Ley General de Educación como el instrumento que regula la prestación del servicio educativo.")

    add_heading_3(doc, "7.11.1 Compromisos y obligaciones jurídicas en el ámbito nacional")
    add_styled_paragraph(doc, "La Constitución de la República de El Salvador establece los fines generales de la educación y constituye el marco jurídico sobre el cual se desarrollan las leyes y políticas educativas del país.")
    add_styled_paragraph(doc, "Por su parte, la Ley General de Educación regula la prestación del servicio educativo en las instituciones oficiales y privadas y desarrolla las responsabilidades relacionadas con el funcionamiento y organización del sistema educativo. SITEAL identifica esta legislación como parte de los compromisos y obligaciones nacionales asumidos por el Estado salvadoreño para garantizar el derecho a la educación.")
    add_styled_paragraph(doc, "Este marco permite contextualizar institucionalmente la presente investigación, entendiendo que la infraestructura tecnológica y los servicios de soporte asociados al ámbito educativo forman parte de los recursos utilizados para apoyar el funcionamiento de dicho sistema.")

    add_heading_3(doc, "7.11.2 Planificación de la educación")
    add_styled_paragraph(doc, "La planificación educativa permite trasladar los principios y obligaciones establecidos en el marco jurídico hacia planes, estrategias, programas y líneas de acción.")
    add_styled_paragraph(doc, "SITEAL señala que el Plan Sectorial de Educación 2022-2030 establece prioridades, programas y líneas de acción para el sistema educativo salvadoreño, además de contemplar aspectos relacionados con costos, financiamiento, planificación operativa, monitoreo y evaluación.")
    add_styled_paragraph(doc, "La consideración de la planificación educativa dentro de esta investigación permite situar la infraestructura tecnológica de la Sede de Enlaces con la Educación dentro de un contexto institucional más amplio, en el cual los recursos tecnológicos constituyen elementos que apoyan las actividades y servicios del sector educativo.")

    add_heading_3(doc, "7.11.3 Caracterización de la política educativa nacional")
    add_styled_paragraph(doc, "La política educativa nacional comprende las diferentes acciones mediante las cuales el Estado busca garantizar el funcionamiento del sistema educativo y el ejercicio del derecho a la educación.")
    add_styled_paragraph(doc, "SITEAL caracteriza estas acciones considerando, entre otros componentes, el currículo y los modelos de gestión institucional, los docentes y la infraestructura, tecnología y equipamiento. En este último ámbito se incluyen las acciones dirigidas a mantener, ampliar, rehabilitar, equipar y dotar de tecnología a los servicios educativos.")
    add_styled_paragraph(doc, "Esta dimensión guarda relación con el contexto de la investigación dado que la provisión de servicios tecnológicos educativos requiere infraestructura de comunicaciones que permita conectar dispositivos y acceder a recursos digitales. En consecuencia, la seguridad de la red puede analizarse como un componente técnico relacionado con la protección y adecuada administración de dicha infraestructura, sin sustituir ni ampliar las obligaciones establecidas por la normativa educativa.")

    add_heading_2(doc, "7.12 Relación de los fundamentos teóricos con el modelo propuesto")
    add_styled_paragraph(doc, "Los conceptos desarrollados permiten establecer la base teórica para el diseño del modelo de seguridad perimetral y segmentación lógica propuesto para la Sede de Enlaces con la Educación del distrito de Santa Rosa de Lima.")
    add_styled_paragraph(doc, "La segmentación mediante VLAN permitirá plantear la separación lógica de dispositivos de acuerdo con las funciones identificadas durante el diagnóstico. Las ACL y el firewall permitirán establecer políticas para controlar las comunicaciones entre dichos segmentos, mientras que los mecanismos de proxy y HTTPS/TLS permitirán estudiar controles adicionales relacionados con el acceso a servicios y la protección de las comunicaciones.")
    add_styled_paragraph(doc, "La propuesta será estructurada y evaluada dentro de un ambiente simulado en GNS3, conforme a los objetivos definidos en la investigación. Esto permitirá representar la arquitectura propuesta y analizar técnicamente su funcionamiento sin realizar modificaciones directas sobre la infraestructura física de la sede.")
    add_styled_paragraph(doc, "De esta manera, el marco teórico vincula los fundamentos de seguridad informática y redes con las condiciones identificadas en la institución y proporciona los conceptos necesarios para sustentar posteriormente el diseño, implementación simulada y análisis del modelo de seguridad propuesto.")

    # 7. METODOLOGÍA
    add_heading_1(doc, "8. Metodología")
    add_heading_2(doc, "8.1 Tipo y diseño de investigación")
    add_styled_paragraph(doc, "Bajo los criterios metodológicos de Hernández-Sampieri y Mendoza Torres (2023), el estudio adopta un enfoque cuantitativo y un diseño no experimental de corte transversal. No existe manipulación deliberada sobre los conmutadores ni el cableado de la sede; los parámetros técnicos y los flujos de tráfico se registran en su estado operativo habitual dentro del periodo lectivo de 2026.")
    add_styled_paragraph(doc, "La investigación tiene un alcance descriptivo y propositivo (desarrollo tecnológico). En primer término, detalla la topología instalada, la distribución de bocas funcionales y los vectores de exposición que comprometen los datos. Con estos insumos, formula un modelo de seguridad perimetral y segmentación lógica simulado en GNS3, integrando cortafuegos GNU/Linux, particionado en VLANs y control de navegación mediante proxy.")

    add_heading_2(doc, "8.2 Unidad de análisis")
    add_styled_paragraph(doc, "La unidad de análisis corresponde a la red de datos de la Sede de Enlaces con la Educación (distrito de Santa Rosa de Lima, La Unión Norte). El ecosistema operativo enlaza diez computadoras de escritorio asignadas al personal técnico y docente, cuya conectividad converge en un switch central complementado por routers inalámbricos secundarios.")

    add_heading_2(doc, "8.3 Caracterización de la infraestructura actual")
    add_styled_paragraph(doc, "La sede conserva la topología física en estrella montada desde la edificación del inmueble (circa 2003). Su núcleo de conmutación sigue siendo el switch instalado en esa fecha, el cual exhibe un desgaste físico notable: múltiples bocas RJ-45 quedaron inoperativas por deterioro eléctrico, reduciendo los puertos de red estables a una fracción del total original.")
    add_styled_paragraph(doc, "A nivel perimetral, la sede perdió con los años el servidor dedicado y el proxy físico que antiguamente filtraban y balanceaban el acceso hacia el exterior. Para abastecer a los diez técnicos ante la falta de tomas de pared funcionales, se interconectaron routers comerciales que radian señal Wi-Fi hacia varias oficinas. A su vez, el módem del proveedor de telecomunicaciones cuenta con tres salidas físicas ocupadas: una alimenta las cámaras de videovigilancia, otra enlaza un router de distribución y la tercera conecta directamente la máquina de la jefatura de sede.")

    add_heading_2(doc, "8.4 Problemática de seguridad informática")
    add_styled_paragraph(doc, "Esta configuración dispersa genera tres problemas de fondo: ausencia de visibilidad y auditoría centralizada, saturación de puertos deteriorados y tránsito indiscriminado de paquetes entre puestos de trabajo. Al convivir equipos de planta con dispositivos foráneos que ingresan a soporte técnico, la falta de aislamiento eleva el riesgo de contagio por malware y saturación del canal.")

    add_heading_2(doc, "8.5 Técnicas e instrumentos para la recopilación de información")
    add_styled_paragraph(doc, "La recolección de datos combinó observación técnica directa en campo con una encuesta estructurada dirigida al personal operativo de la sede. El instrumento principal consistió en el Cuestionario de Diagnóstico Técnico de Infraestructura de Red (Anexo 3), cuyos siete reactivos analizan tres ejes clave:")

    p_dim1 = doc.add_paragraph()
    p_dim1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_dim1.paragraph_format.left_indent = Inches(0.25)
    p_dim1.paragraph_format.line_spacing = 1.5
    p_dim1.paragraph_format.space_after = Pt(4)
    r_dim1_b = p_dim1.add_run("1. Infraestructura física y conmutación central: ")
    r_dim1_b.bold = True
    r_dim1_b.font.name = 'Arial'
    r_dim1_b.font.size = Pt(11)
    r_dim1_b.font.color.rgb = TEXT_COLOR
    r_dim1_t = p_dim1.add_run("recuento de puestos, estado físico de los puertos del switch matriz y ocupación de bocas en el módem de enlace.")
    r_dim1_t.font.name = 'Arial'
    r_dim1_t.font.size = Pt(11)
    r_dim1_t.font.color.rgb = TEXT_COLOR

    p_dim2 = doc.add_paragraph()
    p_dim2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_dim2.paragraph_format.left_indent = Inches(0.25)
    p_dim2.paragraph_format.line_spacing = 1.5
    p_dim2.paragraph_format.space_after = Pt(4)
    r_dim2_b = p_dim2.add_run("2. Topología y segmentación de red: ")
    r_dim2_b.bold = True
    r_dim2_b.font.name = 'Arial'
    r_dim2_b.font.size = Pt(11)
    r_dim2_b.font.color.rgb = TEXT_COLOR
    r_dim2_t = p_dim2.add_run("esquema de distribución en estrella, presencia de VLANs y mecanismos de contención aplicados a computadoras externas en mantenimiento.")
    r_dim2_t.font.name = 'Arial'
    r_dim2_t.font.size = Pt(11)
    r_dim2_t.font.color.rgb = TEXT_COLOR

    p_dim3 = doc.add_paragraph()
    p_dim3.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_dim3.paragraph_format.left_indent = Inches(0.25)
    p_dim3.paragraph_format.line_spacing = 1.5
    p_dim3.paragraph_format.space_after = Pt(6)
    r_dim3_b = p_dim3.add_run("3. Seguridad perimetral y políticas de tráfico: ")
    r_dim3_b.bold = True
    r_dim3_b.font.name = 'Arial'
    r_dim3_b.font.size = Pt(11)
    r_dim3_b.font.color.rgb = TEXT_COLOR
    r_dim3_t = p_dim3.add_run("existencia de servidores proxy, filtrado de contenido, listas de control de acceso (ACL) y gestión de certificados HTTPS/TLS.")
    r_dim3_t.font.name = 'Arial'
    r_dim3_t.font.size = Pt(11)
    r_dim3_t.font.color.rgb = TEXT_COLOR

    add_styled_paragraph(doc, "La información levantada permitió diagnosticar las condiciones operativas de la sede y construir la matriz de riesgos institucionales.")

    add_heading_2(doc, "8.6 Propuesta tecnológica")
    add_styled_paragraph(doc, "Tomando como base los requerimientos levantados, la solución se estructurará sobre un laboratorio simulado en GNS3. Este entorno recrea la topología sin interferir con las operaciones cotidianas del edificio.")
    add_styled_paragraph(doc, "El diseño proyecta la segmentación lógica mediante VLANs para aislar áreas administrativas, técnicas y de diagnóstico; políticas de filtrado con iptables/nftables en GNU/Linux; traducción de direcciones de red (NAT); y la implementación de un servidor proxy SQUID configurado con certificados HTTPS/TLS para auditar y controlar el tráfico saliente.")

    # 8. ANÁLISIS E INTERPRETACIÓN DE LOS RESULTADOS
    add_heading_1(doc, "9. Análisis e interpretación de los resultados")
    add_styled_paragraph(doc, "El diagnóstico de campo constató que, si bien la red permite la operación básica de los diez puestos de trabajo, presenta vulnerabilidades estructurales críticas derivadas de su diseño plano y de la obsolescencia del hardware central.")
    add_styled_paragraph(doc, "El hallazgo principal radica en la inexistencia de segmentación lógica: toda la sede comparte un único dominio de broadcast. Las computadoras de administración, donde se procesan registros institucionales, conviven en el mismo segmento de red con laptops y tabletas estudiantiles conectadas para diagnóstico o mantenimiento de hardware. Si un equipo externo ingresa comprometido con código malicioso, el tráfico dañino tiene visibilidad directa hacia cualquier nodo de la red interna sin ninguna barrera de contención.")
    add_styled_paragraph(doc, "En el núcleo físico, el switch central arrastra más de dos décadas de operación ininterrumpida. La pérdida progresiva de puertos RJ-45 forzó la instalación empírica de routers secundarios para cubrir las áreas sin tomas de pared, fragmentando la administración física y multiplicando puntos potenciales de fallo.")
    add_styled_paragraph(doc, "En el plano perimetral, la eliminación del servidor y del proxy originales dejó el tráfico huérfano de auditoría. Las conexiones salen directamente por el módem del proveedor hacia Internet sin listas de control de acceso (ACL), sin bloqueo de categorías riesgosas y sin inspección criptográfica sobre canales HTTPS/TLS.")
    add_styled_paragraph(doc, "Estos factores evidencian que las fallas de la sede no obedecen a la cantidad de dispositivos conectados, sino a la falta de aislamiento y control jerárquico. La solución requiere separar el tráfico en tres VLANs operativas (administración, soporte técnico y zona de cuarentena/diagnóstico) y desplegar un cortafuegos Linux con proxy SQUID que supervise el perímetro y bloquee el movimiento lateral no autorizado.")

    # 8.1 MATRIZ DE RIESGOS
    add_heading_2(doc, "9.1 Matriz de Análisis y Evaluación de Riesgos")
    add_styled_paragraph(doc, "Para jerarquizar el impacto de cada vulnerabilidad frente a la tríada de confidencialidad, integridad y disponibilidad (CIA), los hallazgos se consolidaron en la siguiente matriz estructurada:")

    # Matriz Table
    tbl_mat = doc.add_table(rows=6, cols=6)
    tbl_mat.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_mat, color="173864", sz="6", val="single")

    mat_headers = ["Activo", "Amenaza", "Vulnerabilidad", "Probabilidad", "Impacto", "Riesgo"]
    mat_rows = [
        ("Switch Central\n(Topología física)", "Falla de hardware e interrupción masiva del servicio", "Alto grado de obsolescencia (instalado aprox. en 2003) y puertos físicos dañados.", "Alta", "Alto", "Crítico"),
        ("Equipos\nAdministrativos", "Movimiento lateral de malware o accesos no autorizados", "Operación en una red plana (dominio de broadcast único) sin segmentación VLAN.", "Alta", "Alto", "Crítico"),
        ("Equipos en\nDiagnóstico", "Infección por conexión de dispositivos externos comprometidos", "Ausencia de una red o DMZ aislada para soporte técnico.", "Media", "Alto", "Alto"),
        ("Tráfico Saliente", "Acceso a sitios maliciosos o consumo indebido de red", "Desincorporación del servidor central y del proxy SQUID para filtrado perimetral.", "Alta", "Medio", "Alto"),
        ("Conexiones\nInalámbricas", "Interceptación de datos no encriptados (ataque MITM)", "Tránsito de datos sin políticas forzadas de encriptación (HTTPS/TLS).", "Media", "Medio", "Medio")
    ]

    for col_idx, h_text in enumerate(mat_headers):
        c = tbl_mat.rows[0].cells[col_idx]
        c.text = h_text
        set_cell_margins(c, top=80, bottom=80, left=60, right=60)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx >= 3 else WD_ALIGN_PARAGRAPH.LEFT
        p.runs[0].bold = True
        p.runs[0].font.name = 'Arial'
        p.runs[0].font.size = Pt(9.5)
        p.runs[0].font.color.rgb = UNAB_BLUE

    set_row_bottom_border(tbl_mat.rows[0], color="173864", sz="6")

    for r_idx, r_vals in enumerate(mat_rows):
        for col_idx, text in enumerate(r_vals):
            c = tbl_mat.rows[r_idx + 1].cells[col_idx]
            c.text = text
            set_cell_margins(c, top=60, bottom=60, left=60, right=60)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx >= 3 else WD_ALIGN_PARAGRAPH.LEFT
            p.runs[0].font.name = 'Arial'
            p.runs[0].font.size = Pt(8.5)
            if col_idx == 0:
                p.runs[0].bold = True
            elif col_idx == 5:
                p.runs[0].bold = True
                if text == "Crítico":
                    p.runs[0].font.color.rgb = RGBColor(0xB0, 0x00, 0x20)
                elif text == "Alto":
                    p.runs[0].font.color.rgb = RGBColor(0xE6, 0x51, 0x00)
                else:
                    p.runs[0].font.color.rgb = RGBColor(0xFB, 0x8C, 0x00)

    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(4)
    p_cap.paragraph_format.space_after = Pt(10)
    r_cap = p_cap.add_run("Tabla 1. Matriz de análisis y evaluación de riesgos de la infraestructura actual.")
    r_cap.font.name = 'Arial'
    r_cap.font.size = Pt(9)
    r_cap.italic = True
    r_cap.font.color.rgb = TEXT_COLOR

    add_styled_paragraph(doc, "La matriz evidencia que los niveles de mayor severidad se concentran en el conmutador central (riesgo de interrupción total por falla de hardware) y en las estaciones administrativas (riesgo crítico de contaminación lateral). Estos resultados justifican la implementación del modelo perimetral y el esquema de segmentación lógica propuesto.")

    # 9. CONCLUSIONES & 10. RECOMENDACIONES
    add_heading_1(doc, "10. Conclusiones")

    add_heading_1(doc, "11. Recomendaciones")

    # 11. REFERENCIAS BIBLIOGRÁFICAS
    add_heading_1(doc, "12. Referencias bibliográficas")

    apa_refs = [
        ("Chandramouli, R. (2022). ", "Guide to a secure enterprise network landscape ", "(NIST Special Publication 800-215). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-215"),
        ("Cybersecurity and Infrastructure Security Agency. (2022). ", "Layering network security through segmentation. ", "U.S. Department of Homeland Security. https://www.cisa.gov/sites/default/files/2023-01/layering-network-security-segmentation_infographic_508_0.pdf"),
        ("Hernández-Sampieri, R., \& Mendoza Torres, C. P. (2023). ", "Metodología de la investigación: Las rutas cuantitativa, cualitativa y mixta ", "(2.ª ed.). McGraw Hill."),
        ("Instituto Internacional de Planeamiento de la Educación de la UNESCO. (s. f.). El Salvador: Perfil de educación. ", "Sistema de Información de Tendencias Educativas en América Latina (SITEAL). ", "Recuperado el 27 de septiembre de 2026, de https://siteal.iiep.unesco.org/pais/el_salvador")
    ]

    for part1, part2_italic, part3 in apa_refs:
        p_ref = doc.add_paragraph()
        p_ref.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_ref.paragraph_format.left_indent = Inches(0.5)
        p_ref.paragraph_format.first_line_indent = Inches(-0.5)
        p_ref.paragraph_format.line_spacing = 1.5
        p_ref.paragraph_format.space_after = Pt(8)

        r1 = p_ref.add_run(part1)
        r1.font.name = 'Arial'
        r1.font.size = Pt(10)
        r1.font.color.rgb = TEXT_COLOR

        r2 = p_ref.add_run(part2_italic)
        r2.font.name = 'Arial'
        r2.font.size = Pt(10)
        r2.italic = True
        r2.font.color.rgb = TEXT_COLOR

        r3 = p_ref.add_run(part3)
        r3.font.name = 'Arial'
        r3.font.size = Pt(10)
        r3.font.color.rgb = TEXT_COLOR

    # 12. CRONOGRAMA & 13. PRESUPUESTO
    add_heading_1(doc, "13. Cronograma")

    add_heading_1(doc, "14. Presupuesto")

    # 14. ANEXOS
    add_heading_1(doc, "15. Anexos")

    p_anx1_title = add_heading_2(doc, "Anexo 1: Sesión de lectura y análisis metodológico")
    if os.path.exists("assets/img/anexos/reunion-1/horizontal-1.jpeg"):
        p_img1 = doc.add_paragraph()
        p_img1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img1.paragraph_format.space_before = Pt(6)
        p_img1.paragraph_format.space_after = Pt(4)
        p_img1.add_run().add_picture("assets/img/anexos/reunion-1/horizontal-1.jpeg", width=Inches(5.5))

    p_cap1 = doc.add_paragraph()
    p_cap1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap1.paragraph_format.space_after = Pt(14)
    r_cap1 = p_cap1.add_run("Figura 1. Reunión de lectura del libro Metodología de la investigación: las rutas cuantitativa, cualitativa y mixta (Hernández Sampieri).")
    r_cap1.font.name = 'Arial'
    r_cap1.font.size = Pt(9.5)
    r_cap1.italic = True
    r_cap1.font.color.rgb = TEXT_COLOR

    p_anx2_title = add_heading_2(doc, "Anexo 2: Sesión de formulación metodológica y matriz de riesgos (Fase 2)")
    if os.path.exists("assets/img/anexos/reunion-2/foto-2.jpeg"):
        p_img2 = doc.add_paragraph()
        p_img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img2.paragraph_format.space_before = Pt(6)
        p_img2.paragraph_format.space_after = Pt(4)
        p_img2.add_run().add_picture("assets/img/anexos/reunion-2/foto-2.jpeg", width=Inches(5.5))

    p_cap2 = doc.add_paragraph()
    p_cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap2.paragraph_format.space_after = Pt(14)
    r_cap2 = p_cap2.add_run("Figura 2. Reunión de trabajo para el desarrollo del Marco Teórico, Metodología y Análisis de Resultados.")
    r_cap2.font.name = 'Arial'
    r_cap2.font.size = Pt(9.5)
    r_cap2.italic = True
    r_cap2.font.color.rgb = TEXT_COLOR

    p_anx3_title = add_heading_2(doc, "Anexo 3: Instrumento de Recolección de Datos")
    add_styled_paragraph(doc, "Cuestionario de Diagnóstico Técnico de Infraestructura de Red", bold=True)
    add_styled_paragraph(doc, "A continuación se presenta la ficha técnica y la estructura temática del instrumento diseñado para el diagnóstico de la infraestructura de red en la Sede de Enlaces con la Educación (Distrito de Santa Rosa de Lima):")

    table_anx = doc.add_table(rows=6, cols=2)
    table_anx.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_anx.autofit = False
    set_table_borders(table_anx, color="D8DEE8", sz="4", val="single")

    anx_data = [
        ("Nombre del instrumento:", "Cuestionario de Diagnóstico Técnico de Infraestructura de Red"),
        ("Objetivo:", "Levantar información técnica sobre el estado físico, lógico y de seguridad de la red de datos para fundamentar el modelo perimetral propuesto."),
        ("Técnica de recolección:", "Encuesta técnica estructurada."),
        ("Población objetivo:", "Personal técnico y operativo de la Sede de Enlaces con la Educación."),
        ("Estructura temática:", "7 ítems abiertos distribuidos en 3 dimensiones operativas:\n• Dimensión 1 (Física y central): Equipamiento, puertos y distribución del módem (3 ítems).\n• Dimensión 2 (Lógica): Topología en estrella, ausencia de VLANs y soporte a laptops externas (2 ítems).\n• Dimensión 3 (Seguridad perimetral): Servidores proxy, filtrado y políticas de acceso (2 ítems)."),
        ("Evidencia documental:", "Cuestionario físico aplicado y digitalizado con las respuestas recopiladas en campo (Anexo_3_Cuestionario_Diagnostico_Aplicado.pdf), complementado con el formato técnico en blanco (Instrumento_Cuestionario_Diagnostico_Tecnico.pdf).")
    ]

    for row_idx, (k, val) in enumerate(anx_data):
        row = table_anx.rows[row_idx]
        cell_lbl = row.cells[0]
        cell_val = row.cells[1]

        cell_lbl.width = Inches(2.3)
        cell_val.width = Inches(4.2)

        set_cell_margins(cell_lbl, top=100, bottom=100, left=140, right=140)
        set_cell_margins(cell_val, top=100, bottom=100, left=140, right=140)

        p_lbl = cell_lbl.paragraphs[0]
        p_lbl.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_lbl.paragraph_format.line_spacing = 1.15
        p_lbl.paragraph_format.space_after = Pt(2)
        r_l = p_lbl.add_run(k)
        r_l.font.name = 'Arial'
        r_l.font.size = Pt(10)
        r_l.bold = True
        r_l.font.color.rgb = RGBColor(0x17, 0x38, 0x64)

        p_val = cell_val.paragraphs[0]
        p_val.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_val.paragraph_format.line_spacing = 1.15
        p_val.paragraph_format.space_after = Pt(2)
        r_v = p_val.add_run(val)
        r_v.font.name = 'Arial'
        r_v.font.size = Pt(10)
        r_v.font.color.rgb = TEXT_COLOR

    p_cap_anx = doc.add_paragraph()
    p_cap_anx.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap_anx.paragraph_format.space_before = Pt(6)
    p_cap_anx.paragraph_format.space_after = Pt(14)
    r_cap_anx = p_cap_anx.add_run("Tabla 2. Ficha técnica del instrumento de recolección de datos.")
    r_cap_anx.font.name = 'Arial'
    r_cap_anx.font.size = Pt(9.5)
    r_cap_anx.italic = True
    r_cap_anx.font.color.rgb = TEXT_COLOR

    scan_pages = [
        ("assets/img/anexos/cuestionario/pagina-1.png", "Figura 3. Evidencia de aplicación de instrumento - Página 1 (Información general y Dimensión 1)."),
        ("assets/img/anexos/cuestionario/pagina-2.png", "Figura 4. Evidencia de aplicación de instrumento - Página 2 (Dimensiones 1 y 2)."),
        ("assets/img/anexos/cuestionario/pagina-3.png", "Figura 5. Evidencia de aplicación de instrumento - Página 3 (Dimensión 3).")
    ]
    for img_path, cap_text in scan_pages:
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(4)
            p_img.add_run().add_picture(img_path, width=Inches(5.2))

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(14)
            r_cap = p_cap.add_run(cap_text)
            r_cap.font.name = 'Arial'
            r_cap.font.size = Pt(9.5)
            r_cap.italic = True
            r_cap.font.color.rgb = TEXT_COLOR

    out_file = "2026_II_SeguridadPerimetral_y_AseguramientoRedDatos/Documento_de_Avance_Fase2.docx"
    doc.save(out_file)
    print(f"Documento generado exitosamente con formato idéntico: {out_file}")

if __name__ == '__main__':
    create_document()
