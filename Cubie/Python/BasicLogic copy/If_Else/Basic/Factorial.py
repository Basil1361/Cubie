x = int(input("Enter a value: "))

def product():
    result = 1
    if x == 0:
        print(f"Factorial of {x} is 1")
    else:
        for i in range(1, x + 1):
            result *= i
        return print(f"Factorial of {x} is {result}")
    
product()