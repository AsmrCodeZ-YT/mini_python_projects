import PyPDF2
import os

pdf_path = input("Enter PDF ::: ")
TrueName = os.path.basename(pdf_path)[:-4]
# text file 
txtpath = f"{TrueName}.txt"


pdf_obj = open(pdf_path, "rb")
pdf_read = PyPDF2.PdfReader(pdf_obj)

x = len(pdf_read.pages)


for i in range(x):
    page_obj = pdf_read.pages[i]

    # open text file
    with open(txtpath ,"a+") as f:
        f.write((page_obj.extract_text()))

    print(page_obj.extract_text())

pdf_obj.close()