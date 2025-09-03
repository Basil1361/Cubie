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
    return factorial(n) // factorial(n - r)

# Test the permutation
result = P(5, 3)
print(f"P(5,3) = {result}")  # Should output 60