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
from time import sleep
import easygui
import Wordlister_Package.wlp_main
import os


''' The Text Input '''
def text_extractor():
    '''---------------------
        User Input : The Text file name
        ----------------------'''
    #ui_filename = input("Enter the name of the file without the '.txt': ")
    selection = easygui.fileopenbox()
    # Cleaning up the file name.
    ui_filename = os.path.basename(selection)
    print("One moment, reading ", ui_filename)
    sleep(1)

    #-- Open and Read the file.
    TheFile = open(ui_filename, 'r')
    #-- Extracting the text into a variable.
    text = TheFile.readline()
    TheFile.close()

    #-- To remove any special characters attached to a word
    sleep(1)
    print("Removing punctuations and special characters.")
    translator = str.maketrans('', '', string.punctuation)
    new_text = text.translate(translator)

    #-- Creating an Empty wordlist
    wl =[]
    #-- Appending non-duplicates into the list.
    for word in new_text.split():
        if word not in wl:
            wl.append(word) #-- Add the word to wl
            wl.sort() #-- To Alphabetize



    #-- Info for the user
    sleep(1)
    print("Removing the duplicates.")
    sleep(1)
    print("Creating your text file.")


    #-- Creating the Text File
    with open(ui_filename+"_Wordlist.txt", 'a') as f:
        for x in wl:
            if x.isalpha():
                print(x, file=f)
            else:
                pass
        f.close()
        sleep(1)
        print("[- - - Your Wordlist Is Ready - - -] "
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
    text_extractor()
