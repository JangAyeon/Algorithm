import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(row)]
#print(row, col, graph)

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x,y):
    que = deque()
    que.append([x,y])
    while que:
        x,y = que.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if 0<=nx<row and 0<=ny<col and graph[nx][ny]==1:
                que.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                    
    return graph[row-1][col-1]


print(bfs(0,0))

"""
4 6
101111
101010
101011
111011

15
"""