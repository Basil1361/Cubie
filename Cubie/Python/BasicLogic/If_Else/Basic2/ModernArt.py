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
        s = random.randint(3, 10)  
        p = random.randint(5, 100)  
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

def main(n):
    screen = Screen()
    screen.colormode(255) # tom.colormode(255 works but not here apparently.)
    tom = Turtle()
    tom.shape("turtle")
    tom.speed(0)
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        tom.color(r, g, b)
        Pathways(tom)  
    screen.mainloop()

main(200)
