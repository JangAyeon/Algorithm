import sys
input = sys.stdin.readline
from collections import deque


n,m = map(int, input().split())

visited = [[False for _ in range(m)] for _ in range(n)]
graph=[list(map(int, input().split())) for _ in range(n)]

directions=[[-1,0],[1,0],[0,1],[0,-1],[-1,1],[-1,-1],[1,-1],[1,1]]
answer = 0

def bfs(i,j):
    que = deque()
    que.append([i,j])
    visited[i][j]=True
    while que:
        r,c = que.popleft()
        for dr, dc in directions:
            nr,nc=r+dr,c+dc
            ## 범위 나간 경우 // 이미 방문했던 경우 // 그래프상 1 아닌 경우
            if not(0<=nr<n) or not(0<=nc<m) or graph[nr][nc]!=1 or visited[nr][nc]==True:
                continue
            visited[nr][nc]=True
            que.append([nr, nc])

for i in range(n):
    for j in range(m):
        if not(visited[i][j]) and graph[i][j]==1:
            bfs(i,j)
            ###print(i,j)
            answer+=1

print(answer)
