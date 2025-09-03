# Given that the Fibonacci Sequence starts with 0 and 1. Then the next number of the sequence is the sum of the two numbers before it. Below is the Fibonacci Sequence.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, ...
# Create a program that reads a number, data from input().
# Check whether the inputted numbers belong to the number from the Fibonacci sequence.
# If it is a number from the Fibonacci sequence, print('It is a number from Fibonacci sequence')
# else, print('The number inserted does not belong to the Fibonacci sequence')


# One of the most important notes about the Fibonacci number (N) is that it is a perfect square when 
# 5
# N
# 2
# +
# 4
# 5N 
# 2
#  +4 or 
# 5
# N
# 2
# –
# 4
# 5N 
# 2
#  –4.

# Meaning, 
# 5
# N
# 2
# +
# 4
# 5N 
# 2
#  +4 == perfect square

# Create a function named isPerfectSquare(). This function will return True or False to find the perfect square of the number.
# make your function read a parameter, n
# then, square root the input parameter (n) and assign it to another variable.
# lastly, compare them to return the result

def isPerfectSquare():
    x = int(input("Enter a value: "))
    formula = (5*x**2 + 4) ** 0.5
    formula2 = (5*x**2 - 4) ** 0.5
    if formula.is_integer() or formula2.is_integer():
        print(f"{x} is a Fibonacci number")
    else:
        print(f"{x} is not a Fibonacci number")

isPerfectSquare()

