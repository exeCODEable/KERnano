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

# imports
from time import sleep

# Importing local files.
import General_Tools.chmoder # CHMODER
import General_Tools.leet_speak # De-1337-er
import General_Tools.nmaker # CTF Note Maker


# Kernano Package:
# Error Handling - The Int Checker
import Kernano_Package.Error_Handler
# The Kernanon Menu & Exit Kernano functions
import Kernano_Package.kp_main

# Importing this


# ------------------------------------------------------------
# General Menu Function
def gen_menu():
    print(
"""
+-+-+-+-+-+-+-+-+-+-+
| General Tools Menu|
+-+-+-+-+-+-+-+-+-+-+

[1] CHMODER. (helps you with CHMOD codes)
[2] DE-1337-ER. (l33t sp34k to text & vice versa)
[3] CTF Note Maker.
[4] Back to KERnano Menu.
[5] Exit KERnano. """)

    # sleep for a second
    sleep(1)

    # Getting user input
    ui_gen_menu = int(input("\nEnter Option: "))

    # Send to The Checker for Error Handling
    # Re-assign the User's input with the value returned from The Checker
    ui_gen_menu = Kernano_Package.Error_Handler.the_int_checker(ui_gen_menu)

    if ui_gen_menu == 1:
        # CHMODER Menu
        General_Tools.chmoder.chmod()
    elif ui_gen_menu == 2:
        # DE-1337-ER Menu
        General_Tools.leet_speak.leeter_menu()
    elif ui_gen_menu == 3:
        General_Tools.nmaker.note_maker()
    elif ui_gen_menu == 4:
        # Go back to Kernano's Main Menu
        Kernano_Package.kp_main.kernano_menu()

        # If User Input is rejected by the Error Handler
    elif ui_gen_menu == -1:
        # Go back to the Tool Menu ()
        gen_menu()
    elif ui_gen_menu == -2:
        # Go back to the Tool Menu ()
        gen_menu()
    else:
        # Exit the program
        Kernano_Package.kp_main.exit_kernano()


# End of General Menu function.
# ------------------------------------------------------------



# Calling function with Main Guard.
if __name__ == '__main__':
    gen_menu()