import sys
input = sys.stdin.readline
from collections import deque


R,C = map(int, input().split())

visited = [[[0,0] for _ in range(C)] for _ in range(R)]
sR,sC = map(int, input().split())
sR -=1
sC-=1

eR,eC = map(int, input().split())
eR-=1
eC-=1

graph = []
for _ in range(R):
   graph.append(list(map(int, input().split())))


dr=[-1,1,0,0]
dc=[0,0,-1,1]



def bfs():
    que = deque()
    que.append([sR,sC,0])
    while que:
        r,c, break_ = que.popleft()
        if (r,c)==(eR, eC):
            return visited[r][c][break_]
        for idx in range(4):
            nr,nc = r+dr[idx],c+dc[idx]
            if not(0<=nr<R) or not(0<=nc<C):
                ## print("R 영역", nr, nc)
                continue
            if graph[nr][nc]==0 and visited[nr][nc][break_]==0:
                visited[nr][nc][break_]=visited[r][c][break_]+1
                que.append([nr, nc, break_])
            elif graph[nr][nc]==1 and break_==0 and visited[nr][nc][1]==0:
                visited[nr][nc][1]=visited[r][c][0]+1
                que.append([nr, nc, 1])
    
    return -1



print(bfs())

