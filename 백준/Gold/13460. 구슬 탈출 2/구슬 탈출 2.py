import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
dir = [[-1,0],[+1, 0],[0,-1],[0,1]]
visited = [[[[False for _ in range(M)] for _ in range(N)]for _ in range(M)]for _ in range(N)]


### 시작점 찾기
rStart = []
bStart= []
for r in range(N):
    for c in range(M):
        if graph[r][c]=="R":
            rStart=[r,c]
        if graph[r][c]=="B":
            bStart = [r,c]

def bfs(rr, rc, br,bc):
    que = deque()
    que.append([rr, rc, br,bc, 0])
    visited[rr][rc][br][bc]=True
    while que:
        rr,rc,br,bc,count = que.popleft()

        if count>10:
            return -1
        if graph[rr][rc]=="O":
            
            return count

        for dr, dc in dir:
            ## 빨간색 이동
            # RED
            nrr, nrc = rr, rc
            while True:
                nrr += dr
                nrc += dc
                # 탈출조건1 - 벽
                if graph[nrr][nrc] == '#':
                    nrr -= dr
                    nrc -=dc
                    break
                # 탈출조건2 - 구멍
                if graph[nrr][nrc] == 'O':
                    break
            ## 파란색 이동
            nbr, nbc = br, bc
            while True:
                nbr+=dr
                nbc+=dc
                if graph[nbr][nbc]=="O":
                    break
                if graph[nbr][nbc]=="#":
                    nbr-=dr
                    nbc-=dc
                    break
            
            if graph[nbr][nbc]=="O":
                continue
            if (nbr==nrr) and (nrc == nbc):
                if (abs(rr-nrr)+abs(rc-nrc))>(abs(br-nbr)+abs(bc-nbc)):
                    nrr-=dr
                    nrc-=dc
                else:
                    nbr-=dr
                    nbc-=dc
            if not(visited[nrr][nrc][nbr][nbc]):
                visited[nrr][nrc][nbr][nbc]=True
                que.append([nrr,nrc,nbr,nbc, count+1])
    return -1
print(bfs(rStart[0], rStart[1], bStart[0],bStart[1]))