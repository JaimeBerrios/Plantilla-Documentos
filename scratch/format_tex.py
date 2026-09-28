import re

with open("info/borrador_extracted.txt", "r") as f:
    text = f.read()

# Find the second occurrence of 7. MARCO TEÓRICO
parts = text.split("7. MARCO TEÓRICO")
if len(parts) >= 3:
    content = "7. MARCO TEÓRICO" + parts[2]
    # Cut off at "Nota:"
    content = content.split("Nota: el presente documento")[0].strip()
    
    lines = content.split('\n')
    tex_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            tex_lines.append("")
            continue
            
        if re.match(r'^7\. MARCO TEÓRICO', line):
            tex_lines.append(r"\section{Marco teórico}")
        elif re.match(r'^8\. METODOLOGÍA', line):
            tex_lines.append(r"\section{Metodología}")
        elif m := re.match(r'^\d+\.\d+\.\d+\.\s*(.+)', line):
            tex_lines.append(f"\\subsubsection{{{m.group(1)}}}")
        elif m := re.match(r'^\d+\.\d+\.\s*(.+)', line):
            tex_lines.append(f"\\subsection{{{m.group(1)}}}")
        else:
            line = line.replace('%', r'\%').replace('&', r'\&')
            tex_lines.append(line)
            
    with open("scratch/replacement.tex", "w") as f:
        f.write("\n".join(tex_lines))
    print("Success")
else:
    print("Not found")

