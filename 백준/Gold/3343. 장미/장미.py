import sys
input = sys.stdin.readline
from math import ceil
 

 
N,AC,AP,BC,BP = map(int,input().split())

## 가성비 안 좋은 것이 A 됨
if AP/AC < BP/BC:
    AC,AP,BC,BP = BC,BP,AC,AP
 
 
answer = float('inf')
 
for A_COUNT in range(BC):
    B_COUNT = ceil((N-A_COUNT*AC)/BC)
    isover = False
    answer = min(answer, A_COUNT*AP + B_COUNT*BP)
    if B_COUNT<=0:
        break

print(answer)