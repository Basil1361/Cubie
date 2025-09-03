def collinear(p1, p2, p3):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3
    formula1 = (x1-x3)/(x1-x2)
    formula2 = (y1-y3)/(y1-y2)
    formula3 = (z1-z3)/(z1-z2)
    if formula1 == formula2 == formula3:
        print("Collinear")
    else:    
        print("Different gradient")
    return (formula1, formula2, formula3)

collinear((-1, -2, 1), (1, 2, 3), (4, 8, 6))
collinear((3, 5.4, 3), (1, 6, 2), (5, 12, 3))

