x = int(input("Enter a Number: "))

def primes():
    if x <= 1:
        print("it's not a prime number")
        return
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            print("it's not a prime number")
            return
    print("it's a prime number")

primes()