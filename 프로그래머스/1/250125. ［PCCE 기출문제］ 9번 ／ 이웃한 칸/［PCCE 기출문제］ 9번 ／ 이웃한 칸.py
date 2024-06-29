def solution(board, h, w):
    answer = 0
    target = board[h][w]
    n = len(board)
    for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
        nr, nc = h+dr,w+dc
        if not(0<=nr<n) or not(0<=nc<n) or board[nr][nc]!=target:
            continue
        answer+=1
    ##print(target)
    return answer