def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def P(n, r):
    if n < r:
        return 0
    return factorial(n) // (factorial(n - r) * factorial(r))

AnswerA = P(10, 3)
AnswerB = P(30, 10)
AnswerC = P(20, 5)
print(f"The Answer is {AnswerA}")
print(f"The Answer is {AnswerB}") 
print(f"The Answer is {AnswerC}")