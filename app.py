import PyPDF4
import pandas as pd

# Open the PDF file
pdf_file = open('2022 DBK Stylebook.pdf', 'rb')

# Read the PDF file
pdf_reader = PyPDF4.PdfFileReader(pdf_file)

# Extract the text from each page of the PDF
text = ''
for page in range(pdf_reader.getNumPages()):
    text += pdf_reader.getPage(page).extractText()

# Split the text into lines
lines = text.split('\n')

# Convert the lines into a data frame
df = pd.DataFrame(lines, columns=['text'])


# Close the PDF file
pdf_file.close()
