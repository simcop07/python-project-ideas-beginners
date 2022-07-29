def is_prime(n):
    """Returns True if n is prime, otherwise False"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))

if is_prime(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")
