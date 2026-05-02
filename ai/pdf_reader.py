import pdfplumber

def extract_text(pdf_path):
    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"
                else:
                    print(f"[Warning] No text found on page {page_num}")

        return text

    except Exception as e:
        print("Error reading PDF:", e)
        return None


if __name__ == "__main__":
    file_path = "data/raw/rbi_kyc.pdf"

    print("\n📄 Reading PDF...\n")

    content = extract_text(file_path)

    if content:
        print("✅ Extraction Successful!\n")
        print("----- Extracted Text Preview -----\n")
        print(content[:1000])   # preview first 1000 characters
    else:
        print("❌ Failed to extract text.")