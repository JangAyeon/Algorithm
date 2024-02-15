import sys
from collections import deque 
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split()) ) for _ in range(n)]
dx,dy = [1,-1,0,0],[0,0,1,-1]

melted = []
ans = 0


def bfs():
    que = deque()
    visited = [[0]*m for _ in range(n)]
    que.append([0,0])
    visited[0][0]=1
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if arr[nx][ny]:
                    arr[nx][ny]+=1
                else:
                    visited[nx][ny] = 1
                    que.append([nx,ny])




while True:
    flag = False
    bfs()

    for x in range(n):
        for y in range(m):
            if arr[x][y]>=3:
                arr[x][y]=0
            elif arr[x][y]>=1:
                arr[x][y]=1
                flag = True
    ans+=1

    if not flag:
        print(ans)
        break


