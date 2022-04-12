# ----------------------------------------------------------------------#
# Tool Name: Password Remover / for PDF Kit                             #
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
import pikepdf
from time import sleep
import easygui
import os
import pdfk_main

def pdf_decrypt():
    print("\nPDF Password Remover"
          "\n=====================")
    sleep(1)
    # UI:
    ui_slecection = easygui.fileopenbox()
    the_book = os.path.basename(ui_slecection)
    print("Book selected:  "+ the_book)
    the_password = input("The Password: ")

    # Decrpting the file and saving the new one.
    print("\nDecrypting your file now. "
          "\nThis may take a few minutes depending on size.")
    pdf = pikepdf.open(the_book,password=the_password)
    pdf.save('Decrypted_'+the_book)



    # Ask if another file is needed to be decrypted.
    again()


def again():
    again_answer = input("\nDo you have another PDF to De-password? Y/N: ")
    if again_answer.lower() == 'y':
        pdf_decrypt()
    else:
        # Main Menu
        pdfk_main.pdf_kit_menu()




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
    pdf_decrypt()