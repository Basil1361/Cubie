from turtle import Turtle, Screen

def main():
    sc = Screen()
    sc.colormode(255)
    tom = Turtle()
    tom.shape("turtle")
    tom.speed(0)
    tom.color('green')

    def conditions():
        while True:
            choice = int(input("Enter a value: "))
            if choice == 0:
                r = int(input("Enter a radius: "))
                c = input("Enter a colour: ")
                tom.color(c)
                tom.circle(r)
            elif choice == 1:
                h = int(input("Enter a length: "))
                w = int(input("Enter a width: "))
                f = input("Enter a colour: ")
                tom.color(f)
                for _ in range(2):
                    tom.forward(h)
                    tom.left(90)
                    tom.forward(w)
                    tom.left(90)
            elif choice == 2:
                s = int(input("Enter a length side: "))
                g = input("Enter a colour")
                tom.color(g)
                for _ in range(3):
                    tom.forward(s)
                    tom.left(360/3)
            elif choice == 3:
                break
            else:
                pass
                
    conditions()  
    sc.mainloop()
    
main()
        
        