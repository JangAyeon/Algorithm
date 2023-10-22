T =int(input())

for i in range(T):
    n = int(input())
    moves = [(0,1),(1,0),(0,-1),(-1,0)]
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    v = 1
    idx = 0
    r,c = 0,0
    board[r][c]=v
    
    while True:
        dr, dc = moves[(idx)%len(moves)]
        nr, nc = r+dr, c + dc
        #print(nr,nc,v,dr,dc)
        if (0<=nr<n and 0<=nc<n) and  board[nr][nc]==0:
            v+=1
            board[nr][nc]=v
            r,c = nr,nc
            #print("b",nr,nc,v)
        else:
            idx+=1
        if v==n*n:
            break
    print("#"+str(i+1))
    for row in board:
        print(*row)
        