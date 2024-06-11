from collections import deque

dr=[-1,1,0,0]
dc=[0,0,-1,1]

def drawGraph(c1,r1,c2,r2,board):
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            if (r==r1 or r==r2 or c1==c or c2==c) and board[r][c]!=0:
                board[r][c]=1
            else:
                board[r][c]=0
    return board

def bfs(start, end,board):
    que = deque()
    n = len(board)
    visited = [[False for _ in range(n)] for _ in range(n)]
    que.append(start)
    visited[start[0]][start[1]]=True
    while que:
        r,c = que.popleft()
        if [r,c]==end:
            print(board[r][c]//2)
            return board[r][c]//2
        for idx in range(4):
            nr, nc = r+dr[idx],c+dc[idx]
            
            ## 범위 나감 // 이미 방문함 // 테두리 아님
            if not(0<=nr<n) or not(0<=nc<n) or board[nr][nc]!=1 or visited[nr][nc]==True:
                continue
            ##print(nr, nc, board[nr][nc]+board[r][c] )
            que.append([nr, nc])
            visited[nr][nc]=True
            board[nr][nc]+=board[r][c]
    


def solution(rectangles, characterX, characterY, itemX, itemY):
    n = 51*2
    ## 아예 테두리=1, 영역 내부=0, 영역 밖=-1
    board = [[-1 for _ in range(n)] for _ in range(n)]
    for c1,r1,c2,r2 in rectangles:
        board = drawGraph(c1*2, r1*2,c2*2,r2*2, board)
    answer = bfs([characterY*2,characterX*2],[itemY*2,itemX*2] ,board)

    return answer