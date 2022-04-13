# ----------------------------------------------------------------------#
# Tool Name:  CTF Note Taker                                            #
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
from time import sleep
# General Package:
# The General Tools Main menu
import General_Tools.general_main

# Kernano Package:
# Error Handling - I will use both (int & y/n checker)
import Kernano_Package.Error_Handler


# ------------------------------------------------------------
# Note Maker Function
def note_maker():
    print("""
+-+-+-+-+-+-+-+-+-+-+-+
| CTF Note Maker Menu |
+-+-+-+-+-+-+-+-+-+-+-+ """)
    sleep(1)

    # The Ouput file list
    output_file = []
    # Clear the list
    output_file.clear()

    # Message to the user
    print("\nPlease fill out the following prompts.")
    sleep(1)

    # Room Name
    room_name = input("The Room/VM/CTF Name : ")
    # URL
    room_url = input("The Room/VM/CTF URL : ")
    # Number of Tasks
    num_of_tasks = int(input("The number of Tasks/Flags: "))

    # Setting up the room info
    # Add a couple of blank lines for IPs
    room_info =(
"""
******************************
|  - KERnano : NOTE MAKER -  |
******************************
Name: {0} 
URL: {1}
 --//-- 
Your IP: 
Target's IP:
******************
"""
    ).format(room_name, room_url)

    # Append the Output File list
    output_file.append(room_info)

    # Test print the room info
    #print(room_info)

    # Setting up the number of tasks
    for i in range(num_of_tasks):
        tasks=("""
===============
TASK/FLAG # """+str(i+1)+
"""
------------

===============
""")
        # Append the Output File list.
        output_file.append(tasks)


    # --------------
    # OUTPUT FILE
    # --------------
    # Message to the user
    print("\nYour Note is being created.")
    with open(room_name+"_KERnano-Note-Maker.txt", 'a') as f:
        for x in range(len(output_file)):
            print(output_file[x], file=f)
        f.close()

    # Message to the user
    sleep(2)
    print("Your Note is ready.")


    sleep(1)
    # Call the "Again" function.
    again()

# End of Note Maker Function.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Again Function
def again():
    # To ask the user if they would like to create another note
    answer = input("\nWould you like make another note? [y/n]: ")

    # Send to The Checker for Error Handling
    # Re-assign the User's input with the value returned from The Checker
    answer = Kernano_Package.Error_Handler.the_yn_checker(answer)

    # If answer is 'Yes', The handler will return a '1'
    if answer == 1:
        # Call the Note Maker function
        note_maker()
        # If User Input is rejected by the Error Handler
    elif answer == -1:
        # The again menu
        again()
    else:
        # Go back to General Tools Main Menu
        General_Tools.general_main.gen_menu()

# End of Again Function.
# ------------------------------------------------------------






# Function Calls.
if __name__ == '__main__':
    note_maker() # Calling the note maker.