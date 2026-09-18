import os
from pdf2docx import Converter  #Importing Converter class from pdf2docx library

def pdf_to_docx(pdf,doc):  #function for pdf to doc converter
    if not os.path.exists(pdf):  #Checking if the file available or not.
        print("No file found.")
        return  #Stops the programme here if there is no file found
    
    try:
        cv = Converter(pdf) #The file we want to convert.
        cv.convert(doc, start=0, end=None)
        cv.close() #After converting the file to doc closing the Converter()
        print("Pdf converted to Doc.")

    except Exception as e:
        print(f"Error -> {e}") #If fail to convert the file then error message will be shown.

pdf_file_name = input("Enter your PDF file name : ")  
doc_file_name = input("Enter Doc file name that you want to save : ")

pdf_to_docx(f"{pdf_file_name}.pdf",f"{doc_file_name}.docx")  #calling the pdf_to_docx() converter function.
