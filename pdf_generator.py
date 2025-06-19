from reportlab.pdfgen import canvas as pdfgen

pdf_file = pdfgen.Canvas("text_test.pdf")

pdf_file.drawString(72, 720, "Hello, this is a test PDF document.")
pdf_file.drawString(72, 700, "This document is created using ReportLab.")
pdf_file.drawString(72, 680, "You can add more text as needed.")
pdf_file.setFont("Helvetica", 12)
pdf_file.drawString(72, 660, "This is a simple example of PDF generation.")
pdf_file.setFont("Courier", 10)
pdf_file.drawString(72, 640, "ReportLab is a powerful library for creating PDFs in Python.")
pdf_file.setFont("Times-Roman", 14)
pdf_file.drawString(72, 620, "You can customize fonts and styles as needed in your PDF documents.")
pdf_file.save()
print("PDF file created successfully.")