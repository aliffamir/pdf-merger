import sys
from glob import glob
from pypdf import PdfWriter

def merge_pdf(path: str):
    writer = PdfWriter()

    pdfs = [file for file in glob(f"{path}/*.pdf")]

    pdfs.sort()

    for pdf in pdfs:
        writer.append(pdf)

    with open("learncpp.pdf", "wb") as new_file:
        writer.write(new_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python merge.py <folder_path>")
        print("Example: python merge.py /Users/aliffamir/Downloads/learncpp/")
        sys.exit(1)

    folder_path = sys.argv[1]
    print(f"Merging PDFs in folder: {folder_path}")
    merge_pdf(folder_path)
