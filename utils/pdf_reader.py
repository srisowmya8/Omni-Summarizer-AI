import PyPDF2

def extract_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text
