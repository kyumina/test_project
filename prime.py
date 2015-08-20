# prime.py
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True

def nth_prime(n):
    primes = [2,3,5,7,9,11]
    return primes[n]
