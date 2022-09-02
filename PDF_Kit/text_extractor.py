# ----------------------------------------------------------------------#
# Tool Name: Text Extractor / for PDF Kit                               #
# BETA VERSION                                                          #
#  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  #
# Copyright: exeCODEable, 2022                                          #
# Author: Ash Noor (ryn0f1sh.blog)                                      #
#  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  #
# This tool is for educational purposes.                                #
# We do not condone using this tool for any illegal activity.           #
# Make sure you have permission before Pen Testing any entity.          #
#  +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+  #
# Thank you for the support.                                            #
# Happy Hacking & Code The Planet                                       #
# www.exeCODEable.com  |  www.AshNoor.me  |  www.KERnano.com            #
#-----------------------------------------------------------------------#

# IMPORTS
from time import sleep
import pdfplumber
#from bidi.algorithm import get_display   # python-bidi library
import easygui
import os
import PDF_Kit.pdfk_main



''' The PDF Input  '''
# Using PDF Plumber.
def pdf2():
    print("\nPDF Text Extractor"
          "\n===================")
    sleep(1)
    '''---------------------
    User Input : The PDF file name
    ----------------------'''
    # User Input : Name of the PDF file.
    the_selection = easygui.fileopenbox()
    ui_PDFFileName = os.path.basename(the_selection)
    print("\nExtracting File ... "+ui_PDFFileName)
    sleep(2)


    '''-------------------------------- 
    The PDF info extraction Section 
    --------------------------------'''

    # This loops through the whole PDF
    with pdfplumber.open(ui_PDFFileName) as pdf:
        page = pdf.pages
        for i, pg in enumerate(page):
            text = page[i].extract_text()

            # To correct the text direction
            #text_direction = get_display(text)

            # The header on top of each page + the extracted text
            extracted =(f'-- PAGE: {i + 1} -- \n {text} \n\n')

            # To Open, Write & close a text file
            with open(ui_PDFFileName +"_PDFextracted.txt", "a", encoding="utf-8") as text_file:
                # Writing the extracted text to a file.
                text_file.write(extracted)
                text_file.close()


    sleep(1)
    print("PDF text has been extracted.")

# // End of PDF 2 function.














''' The PDF Input  '''
# Using PDF Plumber.
def pdf_extractor():
    print("\nPDF Text Extractor"
          "\n===================")
    sleep(1)
    '''---------------------
    User Input : The PDF file name
    ----------------------'''
    # User Input : Name of the PDF file.
    ui_selection = easygui.fileopenbox()
    ui_PDFFileName = os.path.basename(ui_selection)
    print("Extracting: "+ ui_PDFFileName + '\n')
    sleep(2)


    '''-------------------------------- 
    The PDF info extraction Section 
    --------------------------------'''
    # This loops through the whole PDF
    with pdfplumber.open(ui_PDFFileName) as pdf:
        page = pdf.pages
        for i, pg in enumerate(page):
            text = page[i].extract_text()
            #-- To Reverse the Characters Left to right
            #text = text[::-1]
            extracted =(f'-- PAGE: {i + 1} -- \n {text} \n\n')
            #print(extracted)
            # Write to a text file & close text file
            with open(ui_PDFFileName +"_PDFextracted.txt", "a", encoding="utf-8") as text_file:
                # I need it to print from the bottom of what is saved.
                # Otherwise it will start printing from the last sentence
                # --- SOMETHING GOES HERE TO PRINT IT CORRECTLY ---
                text_file.write(extracted)
                text_file.close()


    sleep(1)
    print("PDF text has been extracted.")

    # Ask if another file is needed to be decrypted.
    again()


def again():
    again_answer = input("\nDo you have another PDF to extract text from? Y/N: ")
    if again_answer.lower() == 'y':
        pdf_extractor()
    else:
        # Main Menu
        PDF_Kit.pdfk_main.pdf_kit_menu()

# // End of PDF Extractor function.



#-----------------------------
# The Exit Function
def exit_function():
    print("\nExiting program."          
          "\nPlease wait.")
    sleep(2)

    xca_signature = """
    __          _____          __   
   / /         / ____|         \ \  
  / /  __  __ | |        __ _   \ \ 
 < <   \ \/ / | |       / _` |   > >
  \ \   >  <  | |____  | (_| |  / / 
   \_\ /_/\_\  \_____|  \__,_| /_/  

         www.exeCODEable.com 
           Code The Planet

"""

    print(xca_signature)
    sleep(1)

    # -- Any Key to Exit --
    input("\n>->-> [ Please press ENTER key to Exit ] <-<-<")
    exit()
# End of the Exit Function
#-----------------------------




# - - - - - - - - - - - - - - - -
# Main Guard to call the function
if __name__ == '__main__':
    pdf_extractor()







