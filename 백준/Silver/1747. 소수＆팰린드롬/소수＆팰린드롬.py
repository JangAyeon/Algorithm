import sys
input = sys.stdin.readline
import math


def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

def isReversed(num):
    arr = list(str(num))
    if arr==arr[::-1]:
        return True
    else:
        return False

n = int(input())

if n==1:
    print(2)
else:
    i = n
    while True:
        if isPrime(i) and isReversed(i):
            print(i)
            break
        else:
            i+=1