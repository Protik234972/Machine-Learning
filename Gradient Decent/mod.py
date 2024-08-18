from PyPDF2 import PdfReader, PdfWriter
import re

# Load the PDF
file_path = "C:\Users\HP\Desktop\ahotush print summary.pdf"
reader = PdfReader(file_path)
writer = PdfWriter()

# Go through each page to find and replace text
for page in reader.pages:
    text = page.extract_text()
    # Replace "ASHUTUS BARUA" with "AB"
    modified_text = re.sub(r'ASHUTUS BARUA', 'AB', text)
    # Create a new page and add the modified text
    writer.add_page(page)

# Save the modified PDF to a new file
output_path = "C:\Users\HP\Desktop\ahotush print summary_Updated.pdf"
with open(output_path, "wb") as output_pdf:
    writer.write(output_pdf)

output_path
