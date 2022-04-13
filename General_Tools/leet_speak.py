# ----------------------------------------------------------------------#
# Tool Name: DE-137-ER                                                  #
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

# Imports

# Kernano Package:
# Error Handling - The Int Checker
from Kernano_Package.Error_Handler import the_int_checker
# The Kernanon Menu & Exit Kernano functions
import Kernano_Package.kp_main


# General Package:
# The General Tools Main menu
import General_Tools.general_main


# ------------------------------------------------------------
# The E-Leet Function
# -- To convert text to l33t sp34k.
def e_l33t ():
    ui_word = input("What to l33t: ")
    lw = ui_word.lower()
    el33ted = lw.replace("e", "3").replace("a", "4").replace("t", "7").replace("s", "5").replace("g", "6").replace("o", "0").replace("i", "1")
    print(el33ted.title())
    internal_loop()

# End of E-Leet function.
# ------------------------------------------------------------



# ------------------------------------------------------------
# The D-Leet Function
# -- to convert l33t back to standard text.
def d_leet ():
    ui_word = input("What to d-leet: ")
    lw = ui_word.lower()
    dleeted = lw.replace("3", "e").replace("4", "a").replace("7", "t").replace("5", "s").replace("6", "g").replace("0", "o").replace("1", "i")
    print(dleeted)
    internal_loop()

# End of D-Leet function.
# ------------------------------------------------------------



# ------------------------------------------------------------
# The DE-1337-er Menu Function
def leeter_menu():
    print("""
+-+-+-+-+-+-+-+-+-+
| DE-1337-ER Menu |
+-+-+-+-+-+-+-+-+-+
-------------------------------------------------------
| To convert text TO and FROM Leet Speak / 1337 sp34k |
-------------------------------------------------------

[1] E-1337.
[2] D-Leet.
[3] Back to General Tools.
[4] Back to KERnano Menu.
    """)

    # Getting user Input
    menu_answer = input("What is your option?: ")

    # Send to The Checker for Error Handling
    # Re-assign the User's input with the value returned from The Checker
    menu_answer = the_int_checker(menu_answer)

    if int(menu_answer) == 1:
        # From text to l33t sp34k
        e_l33t()
    elif int(menu_answer) == 2:
        # From l33t to text
        d_leet()
    elif int(menu_answer) == 3:
        # Go back to General Tools Main Menu
        General_Tools.general_main.gen_menu()
    elif int(menu_answer) == 4:
        # Go back to Kernano's Main Menu
        Kernano_Package.kp_main.kernano_menu()

        # If User Input is rejected by the Error Handler
    elif menu_answer == -1:
        # Go back to the Tool Menu ()
        leeter_menu()
        # If User Input is rejected by the Error Handler
    elif menu_answer == -2:
        # Go back to the Tool Menu ()
        leeter_menu()
    else:
        # Exit the program
        Kernano_Package.kp_main.exit_kernano()



#-- Internal Loop Function
def internal_loop():
    loop_answer = input("\nBack to the De-L33t-er Menu? [y/n] : ")
    if loop_answer.lower()== 'y':
        leeter_menu()
    else:
        # Go back to General Tools Main Menu
        General_Tools.general_main.gen_menu()

# End of DE-1337-er Menu Function
# ------------------------------------------------------------




#-- The Main Guard in ALL the files please.
'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard to prevent it from running when Imported.
if __name__ == '__main__':
    leeter_menu() # The De-1337-ER Menu


