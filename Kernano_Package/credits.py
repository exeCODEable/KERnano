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
# Kernano Package:
# The Mini menu
import Kernano_Package.kp_main
from time import sleep



# ------------------------------------------------------------
# Credit Title function.
def credit_title():
    print("""
+-+-+-+-+-+
| Credits |
+-+-+-+-+-+
""")
    # The credits are in the 'credits.txt' file.
    # Sleep for a couple of seconds.
    sleep(2)


    # Open the text file.
    # Read through the file using a For Loop.
    # Strip the newline '\n' at the end of each line.
    #close the file
    with open("credits.txt", 'r') as f:
        for line in f:
            print(line.strip())
    f.close()

    # Sleep for a few seconds.
    sleep(2)

    # Call the Mini Menu
    Kernano_Package.kp_main.mini_menu()

# End of Credit Title function.
# ------------------------------------------------------------




# Main Guard to call the function.
if __name__ == '__main__':
    credit_title()