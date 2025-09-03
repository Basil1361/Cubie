import math

def radius(dx,dy):
    formula = (dx**2 + dy**2)**0.5
    return formula

def random():
    dx = int(input("Enter dx: "))
    dy = int(input("Enter dy: "))
    formula = (dx**2 + dy**2)**0.5
    return formula

if random() > radius((50*math.sqrt(2)),(50*math.sqrt(2))):
    print("Outside Circle")
else:
    print("Inside Circle")

