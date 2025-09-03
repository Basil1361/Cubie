from turtle import Turtle, Screen

def main():
    screen = Screen()
    tom = Turtle()
    tom.shape("turtle")
    tom.color("green")
    screen.mainloop()  # keeps the window open


main()
import random

def main():
    screen = Screen()
    screen.setup(700, 700) 

    tom = Turtle()
    tom.shape("turtle")
    tom.speed(0)
    tom.penup()
    tom.goto(0, 0)
    tom.pendown()

    def reset_origin():
        tom.penup()
        tom.goto(0, 0)
        tom.pendown()

    for _ in range(100):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        # color green if strictly inside, red if on the border
        if -200 < x < 200 and -200 < y < 200:
            tom.color("green")
        else:
            tom.color("red")
        tom.goto(x, y)
        reset_origin()

    screen.mainloop()
    
main()
