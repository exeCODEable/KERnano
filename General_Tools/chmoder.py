# ----------------------------------------------------------------------#
# KERnano                                                               #
# The No-Install Python Pen Testing Kit                                                            #
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
# General Package:
# The General Tools Main menu
import General_Tools.general_main


#-----------------------------
# The CHMOD Options Function
def chmod():
    print(
"""
+-+-++-+-+-+-+-+
| CHMODER menu |
+-+-++-+-+-+-+-+ """
    )
    print("-----------------------"
    "\nChoose The Permissions"
    "\n-----------------------"
    "\n1: Execute [--x ]"
    "\n2: Write [ -w- ]"
    "\n3: Execute & Write [ -wx ]"
    "\n4: Read [ r-- ]"
    "\n5: Read & Execute [ r-x ]"
    "\n6: Read & Write [ rw- ]"
    "\n7: Read, Write, & Execute [ rwx ]" "\n")

    # UI's choices.
    # user
    u = int(input(" What is your choice for USER: "))
    
    # group
    g = int(input(" What is your choice for GROUP: "))

    # everyone
    e = int(input(" What is your choice for EVERYONE: "))

    
    # Concacting the code
    uicode = str(u)+str(g)+str(e)
    code = uicode
    vcode = (u, g, e)

    # code test
    #print("\nTest Code:"+ code)    
    
    # Dispalying the numeric results
    print("\nThis Numeric CHMOD code: "+ code)
    
    # Call the visual function
    visual(vcode)

# End of the chmod Function
#-----------------------------




#-----------------------------
# Creating the Visuals of the permissions chosen 
def visual(vcode):  
    print("Will give your file these permissions: ", end="")            
    for x in vcode:
        if (x == 1):
            print("--x", end="")
        elif (x == 2):
            print("-w-", end="")
        elif (x == 3):
            print("-wx", end="")
        elif (x == 4):
            print("r--", end="")
        elif (x == 5):
            print("r-x", end="")
        elif (x == 6):
            print("rw-", end="")
        elif (x == 7):
            print("rwx", end="")
        else:
            print("Invalid Option")
    
    # Call the again function
    again()
# End of the Visual Function
#-----------------------------





#-----------------------------
# Another file
def again():
    # Getting the Y/N answer.
   answer = input("\n\nWould you like help with another code? y/n : " )
   if (answer.lower() == 'y'):
       # call the chmod function again
       chmod()
   else:
       # Go back to General Tools Main Menu
       General_Tools.general_main.gen_menu()

# End of the Again Function
#-----------------------------








'''------------------
CALLING THE FUNCTIONS
----------------------'''
#-- Using a Main Guard call the Title function.
if __name__ == '__main__':
    chmod() # <-- calling the CHMOD choices function

