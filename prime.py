# prime.py

from math import sqrt
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def nth_prime(n):
    count = -1
    num = 0
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1
