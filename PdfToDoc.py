import os
from pdf2docx import Converter

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

pdf_to_docx("Nibir_CV.pdf","Nibir_resume_doc.docx")