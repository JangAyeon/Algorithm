import sys
input = sys.stdin.readline
import math

n = int(input())
##print(n)
isPrime = [False, False] + [True]*(n-1)
seqPrime = []

for i in range(2,n+1):
    if isPrime[i]:
        seqPrime.append(i)
        for j in range(2*i, n+1, i):
            isPrime[j]=False
            

start = end = 0
total = 0
answer = 0
while True:
    if total>=n:
        total-=seqPrime[start]
        start+=1
    elif end==len(seqPrime):
        break
    else:
        total+=seqPrime[end]
        end+=1
    if total==n:
        answer+=1

    ##print(total, start, seqPrime[start], end, seqPrime[end])
print(answer)
    