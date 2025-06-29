import argparse
import os
import re

def markdown_to_html(markdown_text):
    html_lines = []
    in_list = False

    for line in markdown_text.splitlines():
        line = line.strip()

        if not line:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            continue

        # Headings
        if line.startswith("# "):
            html_lines.append(f"<h1>{line[2:].strip()}</h1>")
        elif line.startswith("## "):
            html_lines.append(f"<h2>{line[3:].strip()}</h2>")
        elif line.startswith("### "):
            html_lines.append(f"<h3>{line[4:].strip()}</h3>")

        # Lists
        elif line.startswith("- ") or line.startswith("* "):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{line[2:].strip()}</li>")

        # Paragraphs
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False

            # Inline bold, italics, code
            formatted = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line)
            formatted = re.sub(r"\*(.*?)\*", r"<i>\1</i>", formatted)
            formatted = re.sub(r"`(.*?)`", r"<code>\1</code>", formatted)
            formatted = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', formatted)
            html_lines.append(f"<p>{formatted}</p>")

    if in_list:
        html_lines.append("</ul>")

    return "\n".join(html_lines)

def main():
    parser = argparse.ArgumentParser(description="Markdown to HTML converter")
    parser.add_argument("input", nargs='?', default="input.md", help="Path to input markdown file")
    parser.add_argument("output", nargs='?', default="output.html", help="Path to output HTML file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Input file '{args.input}' not found.")
        return

    with open(args.input, "r", encoding="utf-8") as infile:
        markdown = infile.read()

    html_body = markdown_to_html(markdown)

    html_full = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Markdown to HTML</title>
</head>
<body>
{html_body}
</body>
</html>"""

    with open(args.output, "w", encoding="utf-8") as outfile:
        outfile.write(html_full)

    print(f"✅ Converted '{args.input}' → '{args.output}' successfully.")

if __name__ == "__main__":
    main()
