import random

list_values = []

def random_number():
    for _ in range(15):
        x = random.randint(-100, 100)
        list_values.append(x)
    return list_values

def checking():
    random_number()
    y = int(input("Enter a value: "))
    if y < len(list_values):
        print(list_values[y])
    else:
        print("No values")

checking()
