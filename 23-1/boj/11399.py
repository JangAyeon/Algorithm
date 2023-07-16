import sys
input = sys.stdin.readline

from itertools import permutations

N = int(input().strip())
m =sorted(list(map(int, input().strip().split())))
answer = 0

for idx, i in enumerate(m):
    answer += i*(len(m)-idx)
    
print(answer)