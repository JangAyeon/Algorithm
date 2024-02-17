## https://www.acmicpc.net/problem/18405

import sys
input = sys.stdin.readline
from collections import deque

graph = []
n,k =  map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s,x,y = map(int, input().split())
que = deque()
virus = []
## print(graph, s,x,y)



    
for r in range(len(graph)):
    for c in range(len(graph[0])):
        if (graph[r][c]):
            virus.append([graph[r][c],r,c])
virus.sort()

for v,r,c in virus:
    que.append([r,c,0])

dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs():
    while que:
        r,c, time = que.popleft()
        
        if time ==s:
            continue

        for idx in range(4):
            nr, nc = r + dr[idx], c + dc[idx]
            if not(0<=nr<n) or not(0<=nc<n): ## 범위 벗어나는 경우
                continue
            if graph[nr][nc]==0:
                graph[nr][nc]=graph[r][c]
                que.append([nr, nc, time+1])



bfs()            
print(graph[x-1][y-1])