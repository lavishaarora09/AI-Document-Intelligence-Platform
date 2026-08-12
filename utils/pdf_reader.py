import pdfplumber

def extract_text_from_pdf(uploaded_file):

    text = ""

    total_pages = 0

    with pdfplumber.open(uploaded_file) as pdf:

        total_pages = len(pdf.pages)

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text, total_pages