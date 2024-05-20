import sys
from itertools import permutations

input = sys.stdin.readline
lst = list(input().strip())
n = len(lst)
## print(lst)
answer = set()

def dfs(nums,visited):
    ##print(nums, visited)
    if sum(visited)==n:
        if len(nums)==n:
            answer.add("".join(nums))
        return
    for idx in range(n):
        if not(visited[idx]):
            visited[idx]=1
            if nums[-1]!=lst[idx]:
                dfs(nums+[lst[idx]],visited)
            visited[idx]=0


visited = [0]*(n)
for i in range(n):

    visited[i]=1
    dfs([lst[i]], visited)
    visited[i]=0

print(len(answer))