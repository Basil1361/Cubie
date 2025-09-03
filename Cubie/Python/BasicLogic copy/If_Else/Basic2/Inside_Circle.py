def function():
    R = 10000
    for i in range(10):
        print(f"variable {i+1}" )
        x = int(input("Enter a x variable here: "))
        y = int(input("Enter a y variable here: "))
        if (x**2 + y ** 2) < R**2:
            print("In")
        elif (x**2 + y**2) == R**2:
            print("On the circle line")
        else:
            print("Out")
        
function()
