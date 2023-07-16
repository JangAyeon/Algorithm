import sys
input = sys.stdin.readline

from itertools import permutations

N = int(input().strip())
m =list(map(int, input().strip().split()))

array = list(map(list,permutations(m, len(m))))
temp = array[0]

answer = []
for arr in array:
    total = 0
    for i in range(len(arr)):
        total+=sum(arr[:i+1])
    answer.append(total)
print(min(answer))