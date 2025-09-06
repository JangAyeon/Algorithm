from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def solution(rectangles, characterX, characterY, itemX, itemY):
    n = 102  # 좌표를 2배 확장하므로 (50*2=100 이상 필요)
    board = [[0]*n for _ in range(n)]
    
    # 1. 모든 사각형 채우기
    for x1,y1,x2,y2 in rectangles:
        x1,y1,x2,y2 = x1*2, y1*2, x2*2, y2*2
        for r in range(y1, y2+1):
            for c in range(x1, x2+1):
                board[r][c] = 1
    
    # 2. 내부 부분 지우기
    for x1,y1,x2,y2 in rectangles:
        x1,y1,x2,y2 = x1*2, y1*2, x2*2, y2*2
        for r in range(y1+1, y2):
            for c in range(x1+1, x2):
                board[r][c] = 0
    
    # 3. BFS 탐색
    sx, sy = characterX*2, characterY*2
    ex, ey = itemX*2, itemY*2
    q = deque([(sy, sx, 0)])
    visited = [[False]*n for _ in range(n)]
    visited[sy][sx] = True
    
    while q:
        r,c,d = q.popleft()
        if (r,c) == (ey,ex):
            return d//2  # 좌표를 2배 했으니 다시 절반으로
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and board[nr][nc]==1:
                visited[nr][nc] = True
                q.append((nr,nc,d+1))
