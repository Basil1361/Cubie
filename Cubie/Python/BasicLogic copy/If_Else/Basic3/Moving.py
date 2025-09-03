import random
from turtle import Turtle, Screen

def main():
    sc = Screen()
    sc.colormode(255)
    tom = Turtle()
    tom.shape("turtle")
    tom.penup()
    tom.speed(0)
    tom.color('green')

    def on_click(x, y):
        if -200 < x < 200 and -200 < y < 200:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            tom.color(r,g,b)
            tom.goto(x, y)
        else:
            tom.reset()
            tom.penup()
            tom.shape('turtle')
            tom.color('green')
            tom.speed(0)

    sc.onscreenclick(on_click)
    sc.mainloop()

main()
