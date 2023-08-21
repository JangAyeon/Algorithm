import sys
from itertools import permutations
n,m=map(int, input().split())

arr = sorted(list(map(int, input().split())))

answer = sorted(list(set(permutations(arr,m))))

for i in answer:
    print(*i)
