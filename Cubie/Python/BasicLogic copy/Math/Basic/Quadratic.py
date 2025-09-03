def Quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return print("No real roots")
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return print(f"{root1:.3f}", f"{root2:.3f}")
Quadratic(-6, -2, 6)
Quadratic(1, 4, -21)
Quadratic(1, 3, 4)