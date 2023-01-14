import sys
input=sys.stdin.readline
from collections import deque

dx=[-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]


def bfs(i,j,w,h):
    que = deque()
    que.append((i,j))
    graphs[i][j]=0

    while que:
        x, y = que.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=h or ny<0 or ny>=w:
                continue
            if graphs[nx][ny]:
                graphs[nx][ny]=0
                que.append((nx,ny))
    return 1





while True:
    w,h= map(int, input().split())
    cnt=0

    if w==0 and h==0:
        break

    graphs=[list(map(int, input().split())) for _ in range(h)]


    for i in range(h):
        for j in range(w):
            if graphs[i][j]:
                cnt+=bfs(i,j,w,h)
    print(cnt)
