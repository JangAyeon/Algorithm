from collections import deque


def solution(land):
    n = len(land)
    m = len(land[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    answer = 0
    
    def bfs(r,c, type):
        que = deque([[r,c]])
        visited[r][c]=True
        size = 1
        land[r][c]=type
        while que:
            r,c = que.popleft()
            for nr, nc in [[r-1, c],[r,c-1],[r+1,c],[r,c+1]]:
                ## 범위에 나감 // 이미 방문함
                if not(0<=nr<n) or not(0<=nc<m) or visited[nr][nc]:
                    continue
                if land[nr][nc]==1:
                    visited[nr][nc]=True
                    land[nr][nc]=type
                    size+=1
                    que.append([nr, nc])
        return size
        
    type = 2
    sizeDic={}
    for i in range(n):
        for j in range(m):
            if not(visited[i][j]) and land[i][j]==1:
                sizeDic[type]=bfs(i,j, type)
                type+=1
                

    def getSize(lst):
        size =0
        for k in lst:
            size+=sizeDic[k]
        return size

    for j in range(m):
        temp = []
        for i in range(n):
            if land[i][j]!=0 and land[i][j] not in temp:
                temp.append(land[i][j])
        answer = max(answer, getSize(temp))



            
        
    return answer