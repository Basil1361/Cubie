def product(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sum_n(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


print(product(3) // sum_n(3))
print(product(20) // sum_n(20))
print(product(100) // sum_n(100))