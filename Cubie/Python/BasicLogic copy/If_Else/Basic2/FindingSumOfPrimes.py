def is_prime(k):
    if k < 2:
        return False
    for d in range(2, int(k**0.5) + 1):
        if k % d == 0:
            return False
    return True

total = sum(i for i in range(2, 501) if is_prime(i))
print("Sum of primes up to 500:", total)
