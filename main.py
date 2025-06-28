import argparse
import markdown

def convert_markdown_to_html(input_file, output_file):
    # Read the markdown content
    with open(input_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_content = markdown.markdown(md_content)

    # Wrap in a styled HTML template
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

    # Save the output
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"✅ Converted {input_file} to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown to styled HTML")
    parser.add_argument("input", help="Path to the input markdown file")
    parser.add_argument("output", help="Path to the output HTML file")
    args = parser.parse_args()

    convert_markdown_to_html(args.input, args.output)
