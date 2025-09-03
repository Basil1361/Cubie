# - Minimum length for the password, 6 characters
# - Maximum length for the password, 12 characters.
# - At least 1 lower case letter
# - at least 1 upper case letter
# - must contain at least 1 number
# - At least 1 character from [$#@].
# - the password cannot contain any space
import re

def password_check():
    while True:
        x = input("Type a valid password: ")
        if len(x) < 6:
            print("Minimum length is 6 characters")
            break
        elif len(x) > 12: 
            print("Maximum length is 12 characters")       
            break
        elif not re.search("[A-Z]", x):
            print("At least 1 Upper Case!")             
            break
        elif not re.search("[a-z]", x):
            print("At least 1 Lower Case!")             
            break
        elif not re.search("[0-9]", x):
            print("At least one number")
            break       
        elif not re.search("[$#@]", x):
            print("At least 1 Special Character")             
            break      
        elif " " in x: 
            print("No Spaces!")             
            break
        else:
            print(f"Valid Password! Your Password is now: {x}")
            break
        

        
password_check()        