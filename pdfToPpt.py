from spire.pdf import *

# Open a PDF document
pdf = PdfDocument("/Users/ernandorezende/work/Labs/python/python-basic/Proposta Arquitetura Referencia_v01.0 1.pdf")
# Convert it to PowerPoint PPTX format
pdf.SaveToFile("output.pptx", FileFormat.PPTX)
# Close the document
pdf.Close()