import markdown

# Read the markdown file
with open("input.md", "r", encoding="utf-8") as f:
    md_content = f.read()

# Convert to HTML
html_content = markdown.markdown(md_content)

# Add CSS styles (like link font-size)
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Markdown to HTML</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
        }}
        a {{
            font-size: 20px;
            color: darkblue;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

# Write the final HTML to output.html
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_template)
print("✅ Markdown converted to HTML and saved as output.html")