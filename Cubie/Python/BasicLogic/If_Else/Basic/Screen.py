
x1, x2 = -250, 250 
y1, y2 = -300, 300


def checking():
    for i in range(4):
        print(f"\nCoordinate {i+1}:")

        while True:
            try:
                x = int(input("  Enter x: "))
                break
            except ValueError:
                print("  Type again (whole numbers only)")

        while True:
            try:
                y = int(input("  Enter y: "))
                break
            except ValueError:
                print("  Type again (whole numbers only)")
        
    if x1 < x < x2 and y1 < y < y2:
        print("Within Screen")
    else:
        print("Outside Screen")
        
checking()

