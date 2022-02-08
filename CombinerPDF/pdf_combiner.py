import PyPDF2
import sys

# give a list of pdf files to merge
inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(f"{pdf} is processed")
        merger.append(pdf)
    merger.write("merged.pdf")
    print("all files have been merged into file 'merged.pdf'")

pdf_combiner(inputs)

