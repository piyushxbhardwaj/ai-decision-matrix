import markdown
from xhtml2pdf import pisa
import os

def convert_md_to_pdf():
    md_path = "AI_Decision_Matrix_2026.md"
    pdf_path = "AI_Decision_Matrix_2026.pdf"

    if not os.path.exists(md_path):
        print(f"Error: {md_path} not found.")
        return

    # Read the markdown content
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Convert Markdown to HTML (enable tables and other features)
    html_content = markdown.markdown(md_text, extensions=['tables', 'fenced_code', 'toc'])

    # Print-safe CSS styles suitable for xhtml2pdf
    css_styles = """
    @page {
        size: a4;
        margin: 2.5cm 2cm 2.5cm 2cm;
    }
    body {
        font-family: Helvetica, Arial, sans-serif;
        font-size: 9.5pt;
        line-height: 1.5;
        color: #2b2b2b;
    }
    h1, h2, h3, h4 {
        font-family: Helvetica, Arial, sans-serif;
        color: #111111;
        font-weight: bold;
    }
    h1 {
        font-size: 16pt;
        border-bottom: 1.5px solid #7c3aed;
        padding-bottom: 4px;
        margin-top: 30px;
        page-break-before: always;
    }
    h1:first-of-type {
        page-break-before: avoid;
    }
    h2 {
        font-size: 12.5pt;
        margin-top: 20px;
        color: #3b2b85;
    }
    h3 {
        font-size: 10.5pt;
        margin-top: 14px;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 12px;
        margin-bottom: 12px;
        font-size: 8.5pt;
    }
    th, td {
        border: 1px solid #d3d3d3;
        padding: 6px 8px;
        text-align: left;
    }
    th {
        background-color: #f5f5f7;
        font-weight: bold;
        color: #111111;
    }
    pre, code {
        font-family: Courier, monospace;
        font-size: 8pt;
        background-color: #f7f7f9;
    }
    pre {
        border: 1px solid #e1e1e3;
        padding: 8px;
        margin: 10px 0;
        white-space: pre-wrap;
    }
    blockquote {
        border-left: 3px solid #7c3aed;
        margin-left: 0;
        padding-left: 10px;
        color: #555555;
        font-style: italic;
    }
    hr {
        border: 0;
        border-top: 1px solid #e1e1e3;
        margin: 20px 0;
    }
    p {
        margin-bottom: 10px;
    }
    ul, ol {
        margin-bottom: 10px;
        padding-left: 20px;
    }
    li {
        margin-bottom: 4px;
    }
    
    /* Layout styling for header and footer using fixed positioning */
    #header_content {
        position: fixed;
        top: -1.5cm;
        left: 0;
        right: 0;
        height: 1cm;
        font-family: Helvetica, Arial, sans-serif;
        font-size: 8pt;
        color: #777777;
        border-bottom: 0.5px solid #d3d3d3;
        line-height: 20px;
    }
    
    #footer_content {
        position: fixed;
        bottom: -1.5cm;
        left: 0;
        right: 0;
        height: 1cm;
        font-family: Helvetica, Arial, sans-serif;
        font-size: 8pt;
        color: #777777;
        border-top: 0.5px solid #d3d3d3;
        line-height: 20px;
        text-align: right;
    }
    """

    # Wrap in HTML template with fixed headers/footers
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            {css_styles}
        </style>
    </head>
    <body>
        <div id="header_content">
            AI Decision Matrix 2026 — Executive Reference Guide
        </div>
        <div id="footer_content">
            Page <pdf:pagenumber>
        </div>
        {html_content}
    </body>
    </html>
    """

    # Create PDF output
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(full_html, dest=pdf_file)

    if not pisa_status.err:
        print(f"Success! Created {pdf_path}")
    else:
        print("Error during PDF generation.")

if __name__ == "__main__":
    convert_md_to_pdf()
