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
from time import sleep

# Kernano Package:
# Error Handling - The Int Checker & The YN Checker
from Kernano_Package.Error_Handler import the_int_checker, the_yn_checker
# the Credits
from Kernano_Package.credits import credit_title

# PenTest Package:
#

# PDF Package:
#

# General Package:
#

# Wordlister Package:
# To get the "Wordlist Menu"
# The call : Wordlister_Package.wlp_main.wl_menu()
# This is to prevent a "Circular Import" error.
import Wordlister_Package.wlp_main

# ------------------------------------------------------------
# Title function.
def title():
    print("""
+-+-+-+-+-+-+-+
|   KERnano   |
+-+-+-+-+-+-+-+        
The No-Install Python Pen Testing Kit.
---------------------------------------
    """)
# End of Title function.
# ------------------------------------------------------------




# ------------------------------------------------------------
# Main Menu function.
def kernano_menu():
    print("""
 _ _       _ _    
//\/\\ain  //\/\enu
====================
[1]: Pen Test Tools ... [HLPR / B64 / URL Checker / Nmap]
[2]: PDF Tools ... [Text Extractor / Password Decryptor]
[3]: General Tools ... [CHMODER / DE-133-ER / CTF Note Maker]
[4]: Wordlister ... [Create a wordlist from a text or PDF]
[5]: Credits
[6]: Exit Program.

        """"")
    sleep(1)

    # User Input : Choice of the menu.
    user_menu_selection = input("Enter Your Selection: ")

    # Send to The Checker for Error Handling
    # Re-assign the User's input with the value returned from The Checker
    user_menu_selection = the_int_checker(user_menu_selection)

    # Process based on the value assigned by The Checker.
    if int(user_menu_selection) == 1:
        # Pen Test Tools Menu
        print("Pen Test Tools Menu Goes Here")
    elif int(user_menu_selection) == 2:
        # PDF Tools Menu
        print("PDF Tools Menu Goes Here")
    elif int(user_menu_selection) == 3:
        # General Tools Menu
        print("General Tools Menu Goes Here")
    elif int(user_menu_selection) == 4:
        # Wordlister Menu
        Wordlister_Package.wlp_main.wl_menu()
    elif int(user_menu_selection) == 5:
        # Credits
        credit_title()
        # If User Input is rejected by the Error Handler
    elif user_menu_selection == -1:
        kernano_menu()
        # If User Input is rejected by the Error Handler
    elif user_menu_selection == -2:
        kernano_menu()
    else:
        # Exit Kernano function goes here
        exit_kernano()

# End of Main Menu function.
# ------------------------------------------------------------



# ------------------------------------------------------------
# Mini Menu function.
def mini_menu():
    mm_answer = input("""
 _ _       _ _    
//\/\ini  //\/\enu
==================
(1): Main Menu.
(2): Exit KERnano.
Please select one:  """)

    # Send to The Checker for Error Handling
    # Re-assign the User's input with the value returned from The Checker
    mm_answer = the_int_checker(mm_answer)

    # Process based on the value assigned by The Checker.
    if int(mm_answer) == 1:
        kernano_menu()
    # If User Input is rejected by the Error Handler
    elif mm_answer == -1:
        mini_menu()
    # If User Input is rejected by the Error Handler
    elif mm_answer == -2:
        mini_menu()
    else:
        exit_kernano()
# End of Mini Menu function.
# ------------------------------------------------------------





# ------------------------------------------------------------
# Again function.
# End of Again function.
# ------------------------------------------------------------




# ------------------------------------------------------------
# The Exit Kernano Function
def exit_kernano():
    print("\nThank you for using KERnano by exeCODEable.\nPlease wait.")
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
# End of Exit Kernano Function
# ------------------------------------------------------------