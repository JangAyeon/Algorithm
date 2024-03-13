import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
visited_Not =[[False for _ in range(n)]for _ in range(n)]
visited_Is =[[False for _ in range(n)]for _ in range(n)]
dr= [-1,1,0,0]
dc= [0,0,-1,1]


area_Not = 0
area_Is = 0

def bfs_Not(r,c, type):
    que=deque()
    que.append([r,c])
    visited_Not[r][c]=True
    while que:
        r,c = que.popleft()
        for idx in range(4):
            nr, nc = r+dr[idx], c+dc[idx]
            
            ## 범위 나감
            if not(0<=nr<n) or not(0<=nc<n):
                continue
            
            if not(visited_Not[nr][nc]) and graph[nr][nc]==graph[r][c]:
                que.append([nr, nc])
                visited_Not[nr][nc] = True

def bfs_Is(r,c, type):
    que = deque()
    que.append([r,c])
    while que:
        r,c = que.popleft()
        for idx in range(4):
            nr, nc = r+dr[idx], c+dc[idx]
            
            ## 범위 나감
            if not(0<=nr<n) or not(0<=nc<n):
                continue

            if not(visited_Is[nr][nc]): ## rb, rg, br
                if  (graph[r][c]=="B" and graph[nr][nc]=="B") or (graph[r][c]!="B" and graph[nr][nc]!="B"):
                    que.append([nr, nc])
                    visited_Is[nr][nc]=True
 

for i in range(n):
    for j in range(n):
        if not(visited_Not[i][j]):
            area_Not+=1
            bfs_Not(i, j, graph[i][j])

        if not(visited_Is[i][j]):
            area_Is+=1
            bfs_Is(i,j,graph[i][j])

print(area_Not, area_Is)