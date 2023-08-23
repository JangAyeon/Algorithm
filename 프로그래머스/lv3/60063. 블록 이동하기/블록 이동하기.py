from collections import deque

def setBoard(board):
    n = len(board)
    
    newBoard = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            newBoard[i+1][j+1] = board[i][j]
    return newBoard

def getNext(pos, board):
    # 이동 가능한 위치들
    nextPos = []
    
    pos = list(pos)
    pos1_r, pos1_c = pos[0]
    pos2_r, pos2_c = pos[1]
    
    # 상, 하, 좌, 우
    dr, dc = [-1,1,0,0], [0,0,-1,1]
    for idx in range(4):
        pos1_r_next, pos1_c_next = pos1_r + dr[idx], pos1_c+dc[idx]
        pos2_r_next, pos2_c_next = pos2_r + dr[idx], pos2_c+dc[idx]
        
        if board[pos1_r_next][pos1_c_next]==0 and board[pos2_r_next][pos2_c_next]==0:
            nextPos.append({(pos1_r_next,pos1_c_next),(pos2_r_next,pos2_c_next)})
            
    # 가로로 놓여있는 경우
    if pos1_r==pos2_r:
        for i in [-1,1]:
            if board[pos1_r+i][pos1_c]==0 and board[pos2_r+i][pos2_c]==0:
                nextPos.append({(pos1_r, pos1_c),(pos1_r+i,pos1_c)})
                nextPos.append({(pos2_r, pos2_c),(pos2_r+i,pos2_c)})
    # 세로로 놓여있는 경우
    if pos1_c==pos2_c:
        for i in [-1,1]:
            if board[pos1_r][pos1_c+i]==0 and board[pos2_r][pos2_c+i]==0:
                nextPos.append({(pos1_r, pos1_c),(pos1_r,pos1_c+i)})
                nextPos.append({(pos2_r, pos2_c),(pos2_r,pos2_c+i)})
                
    return nextPos

def solution(board):
    n = len(board)
    board = setBoard(board)
    que = deque()
    visited = []
    pos = {(1,1),(1,2)}
    cost = 0
    que.append((pos,cost))
    visited.append(pos)
    
    while que:
        pos, cost = que.popleft()
        
        if (n,n) in pos:
            return cost
        
        for nextPos in getNext(pos, board):
            if nextPos not in visited:
                que.append((nextPos, cost+1))
                visited.append(nextPos)
                #print(nextPos)
    return 0

#board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
#print(solution(board))