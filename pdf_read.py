from pypdf import PdfReader

reader = PdfReader("text_test.pdf")

page = reader.pages[0]
text = page.extract_text()
print("Extracted text from PDF:")
print(text)
