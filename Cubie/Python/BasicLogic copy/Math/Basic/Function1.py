# Type your code hereimport math
import math

def answer(x,y,z):
    formula = (math.sin(x) * math.sin(y) / x) + y
    formula2 = (math.cos(x) * math.cos(y) + 1)
    formula3 = z * (formula / formula2)
    formula4 = formula3 + 1 - math.e ** z
    return formula4

result = answer(math.pi/6, math.pi/6, 3.4)
print(f"{result:.3f}")

# I didn't change to radians because it is set in default.