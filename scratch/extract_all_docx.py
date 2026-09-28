import zipfile
import xml.etree.ElementTree as ET
import glob
import os

for docx_file in glob.glob("info/*.docx"):
    try:
        with zipfile.ZipFile(docx_file) as z:
            xml_content = z.read('word/document.xml')
            root = ET.fromstring(xml_content)
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            text = '\n\n'.join([''.join([node.text for node in p.findall('.//w:t', ns) if node.text]) for p in root.findall('.//w:p', ns)])
            out_name = docx_file.replace('.docx', '.txt')
            with open(out_name, "w") as f:
                f.write(text)
        print(f"Extracted {docx_file} to {out_name}")
    except Exception as e:
        print(f"Failed to extract {docx_file}: {e}")
