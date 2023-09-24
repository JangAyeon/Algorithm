import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
answer=0
c =sorted([int(input()) for _ in range(n)], reverse=True)
#print(arr, lst)
#print(c)

for idx, value in enumerate(c,1):
    score = value-(idx-1)
    if score<0: score=0
    answer+=score
    #idx=idx+1
    #answer+=value-(idx-1)

        
print(answer)
        