from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

## 덩어리 찾기 - BFS
def bfs(board, target):
    R,C = len(board), len(board[0])
    que = deque()
    blocks = []
    visited = [[False for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if not(visited[i][j]) and board[i][j]==target:
                que.append([i,j])
                visited[i][j]=True
                block=[]
    
    
                while que:
                    r,c = que.popleft()
                    block.append([r,c])
                    for idx in range(4):
                        nr, nc = r+dr[idx],c+dc[idx]
                        ## 범위에 안 속함 // 이미 방문함 // target이 아님
                        if not(0<=nr<R) or not(0<=nc<C) or visited[nr][nc] or board[nr][nc]!=target:
                            continue

                        que.append([nr,nc])
                        visited[nr][nc]=True
                blocks.append(block)
 
    return blocks
    
    


## 주어진 좌표를 (0,0)을 좌측 최상단으로 갖는 배열로 정규화
def regularize(blocks):

    blocks.sort(key=lambda x :x[0])
    minR,maxR = blocks[0][0], blocks[-1][0]
    blocks.sort(key=lambda x :x[1])
    minC,maxC = blocks[0][1], blocks[-1][1]
    R, C = maxR-minR+1, maxC-minC+1
    board = [[0 for _ in range(C)] for _ in range(R)]
    #print(maxR, minR, maxC, minC)
    for r,c in blocks:
        board[r-minR][c-minC]=1
    #for i in board:
    #    print(*i)
    #print("---------------")
    return board
    

## 90회전
def rotate90(board):
    R, C = len(board), len(board[0])
    rotated = [[0 for _ in range(R)] for _ in range(C)]
    for r in range(R):
        for c in range(C):
            rotated[c][R-r-1]=board[r][c]
            
    #for i in rotated:
    #    print(*i)
    return rotated

def solution(game_board, table_board):
    game_blocks = (bfs(game_board,0))
    table_blocks = (bfs(table_board,1))
    answer = 0
    for gb in game_blocks:
        block1 = regularize(gb)
        filled = False
        for tb in table_blocks:
            block2 = regularize(tb)
            
            for _ in range(4):
                block2 = rotate90(block2)
                if block1 == block2:
                    filled = True
                    break
            if filled:
                table_blocks.remove(tb)
                answer+=len(gb)
                break

    return answer