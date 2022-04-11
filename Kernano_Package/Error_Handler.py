# Imports
from time import sleep



"""
-----------------------------------
| Error Handler : The Int Checker |
-----------------------------------
This function is to validate the user's input.
The programs only accepts positive integers.
"The Checker" checks the input sent to it and returns one of three values:
1. Returns back the same value sent (if the input is a positive integer).
2. Returns '-1' (if the input is a negative number).
3. Returns '-2' (if the input is a non-number, i.e. a letter or special character)
Based on the returned value, the function that requested the check then acts accordingly.
-------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

Add the Following to functions that require a positive integer:

# Error Handling : The Checker
import Error_Handler

After asking for user input
# Send to The Checker for Error Handling
# Re-assign the User's input with the value returned from The Checker
Variable = Error_Handler.the_int_checker(Variable)

# Process based on the value assigned by The Checker.
Add these elif statements
# If User Input is rejected by the Error Handler
elif Variable == -1:
    # Reload that functions menu.
    # If User Input is rejected by the Error Handler
elif Variable == -2:
    # Reload that functions menu.
"""

# ///// Beginning of The Integer Checker Function.

def the_int_checker(check_me_please):
    # Using Try & Except for ValueError Handling
    try:
        # If the input is correct.
        if int(check_me_please) > 0:
            # Return the positive value that was sent.
            return check_me_please
        # If the entry is a negative number.
        elif int(check_me_please) < 0:
            print("No negative numbers allowed. \nTry Again.")
            sleep(2)
            return -1
        # If the entry is a negative Zer0.
        elif int(check_me_please) == -0:
            print("No negative numbers allowed. \nTry Again.")
            sleep(2)
            return -1
        else:
            return check_me_please

    except ValueError:
        print("This is not an Integer. \nTry Again.")
        sleep(2)
        return -2

# ///// End of The Integer Checker Function.






"""
--------------------------------------
| Error Handler : The Yes/No Checker |
--------------------------------------
This function is to validate the user's input.
The program only accepts a 'Y' or and 'N' for an answer.
"The Yes/No Checker" checks the input sent to it and returns one of two values:
1. Returns '1' if the answer is 'Y'.
2. Returns '-1' if the answer is anything else.
Based on the returned value, the function that requested the check then acts accordingly.
-------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

Add the Following to all 'again()' functions with a Yes/No menu.
# Error Handling : The Yes/No Checker
import Error_Handler

After asking for user input
# Send to The Checker for Error Handling
# Re-assign the User's input with the value returned from The Checker
Variable = Error_Handler.the_yn_checker(Variable)

# Process based on the value assigned by The Checker.
if Variable == 1:
    # The answer is 'yes', move forward
elif Variable == -1:
    # The answer is an in correct input, and will be taken as a 'no'.
    # Reload that functions menu.
else:
    # The answer is no, exit menu
"""

# ///// Beginning of The Yes/No Checker Function.

def the_yn_checker(check_me_please):
    # Using Try & Except for ValueError Handling
    try:
        # If the input is a 'Y'. Return 1
        if check_me_please.lower() == 'y':
            return 1
    except ValueError:
        # If the input is anything else. Return -1
        return -1

# ///// End of The Yes/No Checker Function.
