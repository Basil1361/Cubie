import random

def guessing():
    x = random.randint(1,9)
    count = 5
    for _ in range(count):
        y = int(input("Enter a Number: "))
        if y != x:
            count -= 1
            print(f"Wrong, remaining chances: {count}")
        if y == x:
            print("Correct")
            break
        if count == 0:
            print("You lost...")
            break
        
guessing()