import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


for r in range(n):
    for c in range(m):
        if r==0 and c+1<m:
            graph[r][c+1]+=graph[r][c]
        elif c==0 and r-1>=0:
            graph[r][c]+=graph[r-1][c] 
        elif 0<=r-1<n and 0<=c-1<m:       
            graph[r][c]+=max(graph[r-1][c], graph[r][c-1])

print(graph[n-1][m-1])