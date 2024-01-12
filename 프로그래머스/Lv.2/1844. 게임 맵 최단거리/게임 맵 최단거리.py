from collections import deque 

def solution(maps):
    
    #maps = [[1, 1]]
    dr, dc = [-1,1,0,0], [0,0,-1,1]
    que = deque()
    que.append([0,0])
    N,M=len(maps), len(maps[0])
    

    while que:
        r,c = que.popleft()
        for idx in range(4):
            nr, nc = r+dr[idx], c + dc[idx]
            ## 범위 밖인 경우 OR 벽인 경우
            if not(0<=nr<N) or not(0<=nc<M) or maps[nr][nc]==0: 
                continue
            ## 최초 방문인 경우 
            if maps[nr][nc]==1:
                maps[nr][nc]=maps[r][c]+1
                que.append([nr,nc])
    
    answer = -1 if maps[-1][-1]==1 else maps[-1][-1]
    return answer