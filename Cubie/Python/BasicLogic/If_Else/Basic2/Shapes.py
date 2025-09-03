import random
from turtle import Turtle, Screen

def Options():
    option = random.randint(0, 2)
    print("chosen option:", option)
    return option

def Pathways(tom):
    option = Options()
    if option == 0:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        d = random.randint(0, 360)
        l = random.randint(10, 200)
        tom.penup()
        tom.goto(x, y)
        tom.pendown()
        tom.setheading(d)
        tom.forward(l)
        return (x, y, d, l)
    elif option == 1:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        s = random.randint(3, 10)  # number of sides
        p = random.randint(5, 100)  # side length
        tom.penup()
        tom.goto(x, y)
        tom.pendown()
        angle = 360 / s
        for _ in range(s):
            tom.forward(p)
            tom.right(angle)
        return (x, y, s, p)
    else: 
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        r = random.randint(5, 100)
        tom.penup()
        tom.goto(x, y)
        tom.pendown()
        tom.circle(r)
        return (x, y, r)

def main():
    screen = Screen()
    tom = Turtle()
    tom.shape("turtle")
    tom.color("green")
    Pathways(tom)
    screen.mainloop()

main()
