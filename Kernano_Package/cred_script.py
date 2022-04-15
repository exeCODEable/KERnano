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

    # The Credits go here.
    print( """
=======
KERnano
=======
Developed & Maintained by: Ash Noor (ryn0f1sh).
www.KERnano.com  | www.AshNoor.com  | www.exeCODEable.com


-------------------------------
I would like to give thanks to:
-------------------------------
-My family, for their love and support.
-Syntax & Luna, for your encouragement and feedback.
-Vernson, for inspiring "The URL Checker".
-Cat, for your support and evangelism, I appreciate you.
-Project Discovery, for being an inspiration for this project.



-------------------------------
I would like to give credit to:
-------------------------------
-Python: For providing the world and I with this superpower.
-All the modules and libraries that made this project possible.
-David Bomble: Who's generous code was the catalyst for the "Port Scanner" feature.



-----------------------------------
A special thank you to my sponsors:
-----------------------------------
Thank you all so very much.   
    """)


    # Call the Mini Menu
    Kernano_Package.kp_main.mini_menu()

# End of Credit Title function.
# ------------------------------------------------------------




# Main Guard to call the function.
if __name__ == '__main__':
    credit_title()