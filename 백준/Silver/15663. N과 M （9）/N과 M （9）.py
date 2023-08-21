import sys
from itertools import permutations
n,m=map(int, input().split())

arr = sorted(list(map(int, input().split())))
visited = [False]*n
answer = []


def dfs(idx, lst):
    
    if idx==m:
        answer.append(lst)
        return
    prev = 0
    for j in range(n):
        if not (visited[j]) and prev!=arr[j]:
            visited[j]=True
            prev = arr[j]
            dfs(idx+1, lst+[arr[j]])
            visited[j]=False
            
    
    

dfs(0, [])
answer.sort()

for i in answer:
    print(*i)
