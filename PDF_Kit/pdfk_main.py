# ----------------------------------------------------------------------#
# Tool Name:  PDF Kit                                                   #
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
#import text_extractor
#import password_remover
import PDF_Kit.text_extractor
import PDF_Kit.password_remover


# Kernano Package:
# Error Handling - The Int Checker
from Kernano_Package.Error_Handler import the_int_checker
# The Kernanon Menu & Exit Kernano functions
import Kernano_Package.kp_main


# ------------------------------------------------------------
# PDF Kit Function
def pdf_kit_menu():
    print("""
+-+-+-+-+-+-+-+-
| PDF Kit Menu |
+-+-+-+-+-+-+-+-

[1] Extract Text.
[2] Password Remover. (You must have the password).
[3] Back to KERnano Menu.
[4] Exit KERnano.   

    """)

    # User Input : Menu Selection
    main_menu_selection = int(input("Select an option: "))

    # Send to The Checker for Error Handling
    # Re-assign the User's input with the value returned from The Checker
    main_menu_selection = the_int_checker(main_menu_selection)

    if main_menu_selection == 1:
        # Go to Text Extractor
        PDF_Kit.text_extractor.pdf_extractor()
    elif main_menu_selection == 2:
        # Go to Password Remover/Decrypter
        PDF_Kit.password_remover.pdf_decrypt()
    elif main_menu_selection == 3:
        # Go back to Kernano's Main Menu
        Kernano_Package.kp_main.kernano_menu()

        # If User Input is rejected by the Error Handler
    elif main_menu_selection == -1:
        # Go back to the menu
        pdf_kit_menu()
        # If User Input is rejected by the Error Handler
    elif main_menu_selection == -2:
        # Go back to the menu
        pdf_kit_menu()
    else:
        # Exit the program
        Kernano_Package.kp_main.exit_kernano()

# End of PDF Kit Menu function.
# ------------------------------------------------------------





# Calling function with Main Guard.
if __name__ == '__main__':
    pdf_kit_menu()


