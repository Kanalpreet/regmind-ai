import fitz
import os


def extract_text_from_pdf(pdf_path):
    """
    Extracts text page-by-page from a PDF.
    """

    # Open PDF
    doc = fitz.open(pdf_path)

    extracted_pages = []

    # Loop through pages
    for page_number in range(len(doc)):

        page = doc[page_number]

        # Extract text
        text = page.get_text()

        # Clean text
        text = text.strip()

        # Skip empty pages
        if not text:
            continue

        # Create metadata structure
        page_data = {
            "document_name": os.path.basename(pdf_path),
            "page_number": page_number + 1,
            "text": text
        }

        extracted_pages.append(page_data)

    return extracted_pages