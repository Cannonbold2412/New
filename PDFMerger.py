from pypdf import PdfWriter

merger = PdfWriter()

files = ["Kiran Nandi Resume.pdf", "Kiran_Adhar_Card.pdf", "Kiran_HSC.pdf", "Kiran_SSC.pdf"]

for file in files:
    merger.append(file)

merger.write("merged.pdf")

merger.close()