import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0

def bfs():
    visited = [[False]*m for _ in range(n)]
    que = deque()
    que.append([0,0])
    visited[0][0] = True
    while que:
        x, y = que.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0<=nx<n and 0<=ny<m and not(visited[nx][ny]):
                if arr[nx][ny]:
                    arr[nx][ny]+=1
                else:
                    visited[nx][ny]= True
                    que.append([nx, ny])



while True:
    flag = False
    bfs()
    for i in range(n):
        for j in range(m):
            if arr[i][j]>2:
                arr[i][j]=0
            elif arr[i][j]>0:
                arr[i][j]=1
                flag = True
    answer+=1
    if not(flag):
        print(answer)
        break
    

