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

# The Imports
from time import sleep

# Importing my custom extraction functions.
from Wordlister_Package.TEXTfunction import text_extractor as tf
from Wordlister_Package.PDFfunction import pdf_extractor as pf


# Kernano Package:
# Error Handling - The Int Checker
from Kernano_Package.Error_Handler import the_int_checker
# The Exit Kernano function
from Kernano_Package.Kernano import kernano_menu, exit_kernano

# ------------------------------------------------------------
# Wordlister Menu function.
def wl_menu():
    # Title and menu options to the user
    print("""
+-+-+-+-+-+-+-+-+-+
| Wordlister Menu |
+-+-+-+-+-+-+-+-+-+

What kind of file are you providing? 
[1] A Text File. (.txt)
[2] A PDF File. (.pdf)
[3] Back to Main Menu.
[4] To Exit KERnano.
""")

    # Getting user input
    ui_wordlister = input("Enter Your Choice: ")

    # Send to The Checker for Error Handling
    # Re-assign the User's input with the value returned from The Checker
    ui_wordlister = the_int_checker(ui_wordlister)

    # User selected "Text File"
    if int(ui_wordlister) == 1:
        # Text File Extraction
        tf()
    elif int(ui_wordlister) == 2:
        # PDF File Extraction
        pf()
    elif int(ui_wordlister) == 3:
        # Go back to Kernano's Main Menu
        kernano_menu()
    # If User Input is rejected by the Error Handler
    elif ui_wordlister == -1:
        # Go back to the Wordlister Menu
        wl_menu()
    # If User Input is rejected by the Error Handler
    elif ui_wordlister == -2:
        # Go back to the Wordlister Menu
        wl_menu()
    else:
        # Exit the program
        exit_kernano()

# End of Wordlister Menu function.
# ------------------------------------------------------------






# Main Guard to call the function.
if __name__ == '__main__':
    wl_menu()