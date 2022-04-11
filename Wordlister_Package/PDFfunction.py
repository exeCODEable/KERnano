# ----------------------------------------------------------------------#
# KERnano                                                               #
# The No-Install Python Pen Testing Kit                                 #
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


# Imports
import string
import pdfplumber
from time import sleep
import easygui
import Wordlister_Package.wlp_main




''' The PDF Input  '''
def pdf_extractor():
    '''--------------------- 
    User Input : The PDF file name
    ----------------------'''
    # User Input : Name of the PDF file.
    # This will bring up a pop up window for the user to find their file.
    ui_PDFFileName = easygui.fileopenbox()

    '''-------------------------------- 
    The PDF info extraction Section 
    --------------------------------'''
    # This loops through the whole PDF
    with pdfplumber.open(ui_PDFFileName) as pdf:
        page = pdf.pages
        for i, pg in enumerate(page):
            text = page[i].extract_text()
            extracted = (f'-- PAGE: {i + 1} -- {text} \n\n')
            # print(extracted)
            # Write to a text file & close text file
            with open("PDFextracted.txt", "a", encoding="utf-8") as text_file:
                text_file.write(extracted)
                text_file.close()

    sleep(1)
    print("PDF text has been extracted.")
    #-- Call the Wordlist creator
    theTextFile(ui_PDFFileName)



'''------------------ 
The Wordlist Creation
---------------------'''
# -- Creating the Text File
def theTextFile (ui_PDFFileName):
    # -- Open and Read the file.
    TheFile = open('PDFextracted.txt', 'r')
    # -- Extracting the text into a variable.
    text = TheFile.read()
    TheFile.close()

    # -- To remove any special characters attached to a word
    translator = str.maketrans('', '', string.punctuation)
    new_text = text.translate(translator)

    # -- Empty list
    wl = []
    # -- Appending non-duplicates into the list.
    for word in new_text.split():
        if word not in wl:
            wl.append(word)  # -- Add the word to wl
            wl.sort()  # -- To Alphabetize

    # -- Info for the user
    sleep(1)
    print("Removing punctuations and special characters.")
    sleep(1)
    print("Removing the duplicates.")
    sleep(1)
    print("Creating your text file.")

    with open(ui_PDFFileName+"_Wordlist.txt", "a") as f:
        for x in wl:
            #cleaned_data = x.translate(str.maketrans('', '', string.punctuation))
            # -- To check if what's on the line is a word 'Alpha' or not.
            if x.isalpha():
                print(x, file=f)
            else:
                pass
    f.close()
    sleep(1)
    print("[- - - Your Wordlist Is Ready - - -]"
          "\n   - - Returning to Wordlister - - ")


    # Sleep for 2 seconds
    sleep(2)
    # Return to Wordlister Menu
    Wordlister_Package.wlp_main.wl_menu()





'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    pdf_extractor()










"""
-------------------
| The Scratch Pad |
-------------------
Slices of codes that was not used.
----------------------------------

#This is only to display it on the screen.
print("The while extract \n", encoded).




"""