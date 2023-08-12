import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
parent=[0]*(n+1)


for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(s):
    que = deque()
    que.append(s)
    while que:
        node = que.popleft()
        for child in graph[node]:
            if parent[child]==0:
                parent[child]=node
                que.append(child)


bfs(1)
print(*parent[2:], sep="\n")
