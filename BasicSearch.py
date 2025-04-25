import math

def isPrime(num):
    ceiling = math.floor(math.sqrt(num)) # this avoids redundently checking over 
    for i in range(2, ceiling):
        if num % i == 0:
            return False
    return True    

def findPossibleMP(n):
    return (2**n)-1

def findMP(totalDesired):
    n = 2
    currAmount = 0
    while currAmount < totalDesired:
        if isPrime(findPossibleMP(n)):
            print(str(currAmount + 1) + ": " + str(findPossibleMP(n)))
            currAmount += 1
        n += 1
        
            
findMP(11)