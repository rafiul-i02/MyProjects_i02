import os
from pdf2docx import Converter

pdf_file_name = input("Enter your PDF file name : ")
doc_file_name = input("Enter Doc file name that you want to save : ")

def pdf_to_docx(pdf,doc):
    if not os.path.exists(pdf):
        print("No file found.")
        return
    
    try:
        cv = Converter(pdf)
        cv.convert(doc, start=0, end=None)
        cv.close()
        print("Pdf converted to Doc.")
    except Exception as e:
        print(f"Error{e}")

pdf_to_docx(pdf_file_name,doc_file_name)
