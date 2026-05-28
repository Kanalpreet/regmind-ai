from ingest.pdf_parser import extract_text_from_pdf

# PDF path
pdf_path = "data/raw/rbi_kyc.pdf"

# Extract pages
pages = extract_text_from_pdf(pdf_path)

# Total pages
print(f"\n✅ Total Pages Extracted: {len(pages)}\n")

# First page preview
print("📄 FIRST PAGE:\n")

print(pages[0])