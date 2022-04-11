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

# Kernano Package:
# To get the "Title" & "Kernano Menu"
# The call : Kernano_Package.Kernano.title() / .kernano_menu()
# This is to prevent a "Circular Import" error.
import Kernano_Package.kp_main
import Kernano_Package






# Main Guard to call the function.
if __name__ == '__main__':
    # Call in the Title function.
    Kernano_Package.kp_main.title()

    # Sleep for a 2 seconds
    sleep(3)

    # Call in the Main Menu function.
    Kernano_Package.kp_main.kernano_menu()


