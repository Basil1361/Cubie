from turtle import Turtle, Screen

def pattern(t, x, y, length, sides, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(sides):
        t.forward(length)
        t.left(360 / sides)

def main():
    sc = Screen()
    sc.colormode(255) 
    tom = Turtle()
    tom.shape("turtle")
    tom.speed(0)

    
    x_positions = [150, -200, 100, -50, 0]
    y_positions = [200, -150, 50, -200, 100]
    lengths = [100, 80, 120, 60, 150]
    sides_list = [3, 4, 5, 6, 8]
    colors = ["blue", "red", "green", "purple", "orange"]

    for i in range(len(x_positions)):
        pattern(tom, x_positions[i], y_positions[i], lengths[i], sides_list[i], colors[i])

    sc.mainloop()

main()
