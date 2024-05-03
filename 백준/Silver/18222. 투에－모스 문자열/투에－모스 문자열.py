import sys
input = sys.stdin.readline
import math

n = int(input())


def recur(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n%2:
        return 1-recur(n//2)
    else:
        return recur(n//2)
    
print(recur(n-1))