import PyPDF2
import os

# Get the path from the user
pdfs_path = input("Enter the path where the PDFs are located: ")

# Initialize the PDF merger
merger = PyPDF2.PdfFileMerger()

# Iterate through PDF files in the specified directory
for file in os.listdir(pdfs_path):
    if file.endswith(".pdf"):
        pdf_file_path = os.path.join(pdfs_path, file)  # Full path to the PDF file
        merger.append(pdf_file_path)

# Specify the output file path
output_file = os.path.join(pdfs_path, "combined.pdf")

# Write the merged PDF to the specified output file
merger.write(output_file)

# Close the merger
merger.close()

print(f"PDFs in {pdfs_path} merged into {output_file}")
