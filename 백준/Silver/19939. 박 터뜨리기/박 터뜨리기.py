import sys
from itertools import combinations
import math
input = sys.stdin.readline

n,m = map(int, input().split())
## print(n,m)

minBall = (1+m)*m/2
if (n<minBall):
    print(-1)
else:
    n-=minBall
    if (n%m==0):
        print(m-1)
    else:
        print(m)