import os
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

def merge_pdfs_with_bookmarks(folder_path, output_filename):
    pdf_merger = PdfMerger()
    pdf_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.pdf') and '综合测评表' in f])

    pdf_writer = PdfWriter()
    current_page = 0

    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        reader = PdfReader(pdf_path)
        
        for i, page in enumerate(reader.pages):
            pdf_writer.add_page(page)
            if i == 0:  # Add a bookmark for the first page of each document
                pdf_writer.add_outline_item(pdf_file, current_page)
        
        current_page += len(reader.pages)

    # Write the final PDF to a file
    output_path = os.path.join(folder_path, output_filename)
    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    print(f"PDFs merged with bookmarks into {output_path}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing the PDFs: ")
    output_filename = input("Enter the output filename (e.g., merged_with_bookmarks.pdf): ")
    merge_pdfs_with_bookmarks(folder_path, output_filename)
