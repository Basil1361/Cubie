# Create variables 3 variables, a, b, and c that reads for an integer input.

# Then make the program that:

# print True if a is in range(-200, 200), otherwise print False,
# print True if b is not in range(-100, 100), otherwise printFalse,
# print False if a or b are not in range(-200, 200), otherwise print False (find the correct logic to describe this),
# print True if a and b are in range(-100, 200), but c is not in this range, otherwise print False.

def range():
    while True:
        try: 
            x = int(input("Enter x: "))
            break
        except ValueError:
            print("Numbers only")
            
    while True:
        try: 
            y = int(input("Enter y: "))
            break
        except ValueError:
            print("Numbers only")
    while True:
        try: 
            z = int(input("Enter z: "))
            break
        except ValueError:
            print("Numbers only")
            
    if -200 < x < 200:
        print("True")
    else:
        print("False")
    if not -100 < y < 100: 
        print("True")
    else:
        print("False")
    if not(-200 < x < 200 or -200 < y < 200):
        print("False")
    else:
        print("True")
    if (-100 < x < 200 and -100 < y < 200) and not -100 < z < 200:
        print("True")
    else:
        print("False")
        
range()