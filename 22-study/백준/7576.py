from collections import deque
import sys
input=sys.stdin.readline

M,N=map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(N)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]
que=deque([])
res=0
flag=False

#print(N,M, graph, visited, dx,dy)


for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            que.append([i,j])

def bfs():
    while que:
        x,y=que.popleft()
        for k in range(4):
            nx, ny=x+dx[k], y+dy[k]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
                que.append([nx, ny])
                graph[nx][ny]=graph[x][y]+1


bfs()
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            flag=True
            break

if flag:
    print(-1)
else:
    print(max(map(max,graph))-1)