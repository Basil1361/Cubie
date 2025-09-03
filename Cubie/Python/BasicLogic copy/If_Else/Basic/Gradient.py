def collinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    formula1 = (y1-y2)/(x1-x2)
    formula2 = (y1-y3)/(x1-x3) 
    if formula1 == formula2:
        print("Collinear")
    else:    
        print("Different gradient")
    return (formula1, formula2)


collinear((-1, -2), (1, 2),(4, 8))
collinear((3, 5.4), (1, 6), (5, 12))




