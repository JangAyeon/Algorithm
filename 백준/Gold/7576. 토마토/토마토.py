#  정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

import sys
from collections import deque
input = sys.stdin.readline

col, row = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]
dx= [-1,0,1,0]
dy = [0,1,0,-1]

que = deque()

def bfs():
    while que:
        x,y = que.popleft()
        for idx in range(4):
            nx, ny = x +dx[idx],y+dy[idx]
            if 0<=nx<row and 0<=ny<col and graph[nx][ny]==0:
                    graph[nx][ny]=graph[x][y]+1
                    que.append([nx,ny])
    
    return graph
    
for i in range(row):
    for j in range(col):
        if graph[i][j]==1:
            que.append([i,j])
            
graph = bfs()
#print(graph)
answer = 1
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
        if answer<j:
            answer = j
print(answer-1)


"""
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
6
"""