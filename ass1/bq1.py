from math import sqrt


def isPrime(n):
    if(n <= 1):
        return False
    for i in range(2, int(sqrt(n))+1):
        if(n % i == 0):
            return False
    return True


n = 10
for i in range(2, n):
    if(isPrime(i)):
        print(i, end=", ")
