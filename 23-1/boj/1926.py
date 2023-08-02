import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]
visited = [[False]*col for _ in range(row)]
#print(row, col,graph)


count = 0 
size = 0
dx = [-1, 0, 1, 0]
dy = [0,1,0,-1]


def bfs(x, y):
    que = deque()
    que.append([x,y])
    visited[x][y]= True
    size = 1
    while que:
        x, y = que.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if 0<=nx<row and 0<=ny<col and not(visited[nx][ny]):
                visited[nx][ny]=True
                if graph[nx][ny]==1:
                    size+=1
                    que.append([nx, ny])
                
    return size

for i in range(row):
    for j in range(col):
        if graph[i][j]==1 and not(visited[i][j]):
            count+=1
            size = max(size, bfs(i,j))
print(count)
print(size)

"""
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

4
9
"""