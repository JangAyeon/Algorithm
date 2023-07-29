import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [1,-1,0,0], [0,0,1,-1]
melted = []
res=0


def dfs():
    que = deque()
    que.append([0,0])
    visited = [[0]*m for _ in range(n)]
    visited[0][0]=1

    while que:
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if arr[nx][ny]:
                      arr[nx][ny]+=1
                else:
                     visited[nx][ny] = 1
                     que.append([nx, ny])
        #print(arr)

while True:
    flag = False
    dfs()
    for i in range(n):
        for j in range(m):
            
            if (arr[i][j]>=3): 
                    arr[i][j]=0
            
            elif (arr[i][j]>=1):
                    arr[i][j]=1
                    flag= True
    res+=1     
    if not flag:
        print(res)
        break