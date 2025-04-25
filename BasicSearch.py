import math

def isPrime(num):
    ceiling = sqrt(num).floor() # this avoids redundently checking over 
    for i in range(2, ceiling):
        if num % i == 0:
            return False
    return True    