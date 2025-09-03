import math

def distance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    printing = print(f"{dist:.3f}")
    return printing


distance(5, -2, 1, -5)
distance(12, 3, -5, 10)
distance(1, 4, 5, 1)