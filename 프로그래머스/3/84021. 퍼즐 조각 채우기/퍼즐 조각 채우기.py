from collections import deque

dr,dc=[-1,1,0,0],[0,0,-1,1]

def bfs(board, target):
    N=len(board)
    visited = [[False for _ in range(N)] for _ in range(N)]
    que = deque()
    spots=[]
    for i in range(N):
        for j in range(N):
            if not(visited[i][j]) and board[i][j]==target:
                que.append([i,j])
                visited[i][j]=True
                spot = []

                while que:
                    r,c = que.popleft()
                    spot.append([r,c])
                    for idx in range(4):
                        nr, nc = r+dr[idx],c+dc[idx]
                        if not(0<=nr<N) or not(0<=nc<N) or visited[nr][nc] or board[nr][nc]!=target: 
                            continue
                        que.append([nr, nc])
                        visited[nr][nc]=True

                spots.append(spot)

    return spots

def regularize(pieces):

    pieces.sort(key=lambda x:x[0])
    maxR,minR = pieces[-1][0],pieces[0][0]
    pieces.sort(key=lambda x:x[1])
    maxC,minC = pieces[-1][1],pieces[0][1]
    board = [[0 for _ in range(maxC-minC+1)] for _ in range(maxR-minR+1)]

    for r,c in pieces:
        board[r-minR][c-minC]=1

    return board

def rotate(board):
    R, C = len(board), len(board[0])
    rotated = [[0 for _ in range(R)] for _ in range(C)]
    for r in range(R):
        for c in range(C):
            rotated[c][R-r-1]=board[r][c]
    return rotated

def solution(game_board, puzzle_board):
    answer = 0
    blanks = bfs(game_board,0)

    puzzles = bfs(puzzle_board,1)
    for blank in blanks:
        reg_blank = regularize(blank)
        flag = False
        for original_puzzle in puzzles:
            puzzle = regularize(original_puzzle)
            for _ in range(4):
                puzzle = rotate(puzzle)
                if puzzle == reg_blank:
                    flag = True
                    break ## 회전 중지
            if flag:
                puzzles.remove(original_puzzle)
                break  ## 퍼즐 탐색 중지
        if flag:
            answer+=len(blank)

            
    
    return answer