import sys
input = sys.stdin.readline
from collections import deque

directions =[[-1,0],[1,0],[0,-1],[0,1]]

## 가로, 세로
n,m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = [[[[False for _ in range(m)] for _ in range(n)]for _ in range(m)]for _ in range(n)]
##print(n,m, board)
r_start = []
b_start = []
for i in range(n):
    for j in range(m):
        if board[i][j]=="R":
            r_start=[i,j]
        elif board[i][j]=="B":
            b_start=[i,j]
            
def bfs(rr,rc,br,bc):
    que = deque()
    que.append([rr,rc,br,bc,0])
    visited[rr][rc][br][bc]=True
    while que:
        rr,rc,br,bc,count=que.popleft()
        if board[rr][rc]=="O": ## 빨간색: 구멍 도달
            return count
        for dr, dc in directions:
            ## 빨간색 움직이기
            nrr, nrc = rr,rc
            while True:
                nrr, nrc = nrr+dr, nrc+dc
                if board[nrr][nrc]=="#":
                    nrr-=dr
                    nrc-=dc
                    break
                if board[nrr][nrc]=="O":
                    break
            ## 파란색 움직이기
            nbr, nbc = br,bc
            while True:
                nbr, nbc = nbr+dr, nbc+dc
                if board[nbr][nbc]=="#":
                    nbr-=dr
                    nbc-=dc
                    break
                if board[nbr][nbc]=="O":
                    break
            if board[nbr][nbc]=="O":
                continue
            if (nrr == nbr) and (nrc==nbc):
                ## 빨간 구슬이 더 멀리서 온 경우
                if abs(nrr-rr)+abs(nrc-rc) > abs(nbr-br)+abs(nbc-bc):
                    nrr-=dr
                    nrc-=dc
                else:
                    nbr-=dr
                    nbc-=dc
            if not(visited[nrr][nrc][nbr][nbc]):
                visited[nrr][nrc][nbr][nbc]=True
                que.append([nrr, nrc, nbr, nbc, count+1])
                
    return -1
    
print(bfs(r_start[0], r_start[1],b_start[0],b_start[1]))
        
    