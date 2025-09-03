import random 

array = []
indexs = [-8, -16, -17, -4, -11]
values = []

def random_values():
    for _ in range(20):
        x = random.randint(-200, 200)
        array.append(x)

def checking():
    random_values()
    print("Full array:", array)  # Show full list

    for idx in indexs:
        # Directly get the value using the negative index
        values.append(array[idx])
    print("Values at given negative indexes:", values)

checking() 