import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
#print(n,m, arr)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

time = 0
result = []

def bfs():
    que = deque()
    que.append([0,0])
    visited = [[False]*m for _ in range(n)]
    count = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==0 and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    que.append([nx, ny])
                elif arr[nx][ny]==1: # 치즈임
                    count+=1
                    arr[nx][ny] = 0
                    visited[nx][ny] = True
    return count
    

while True:
    
    count = bfs()
    result.append(count)
    if count == 0:
        break
    time+=1

print(time)
print(result[-2])
