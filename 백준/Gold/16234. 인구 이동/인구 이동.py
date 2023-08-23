import sys
input = sys.stdin.readline
from collections import deque

n, L, R =map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def findUnion(r,c):
    que = deque()
    que.append([r,c])
    visited[r][c] = True
    union_ = [[r,c]]
    total=graph[r][c]
    while que:
        r,c = que.popleft()
        for idx in range(4):
            nr = r + dr[idx]
            nc = c + dc[idx]
            if not(0<=nr<n) or not(0<=nc<n):
                continue
            if not(visited[nr][nc]) and L<=abs(graph[r][c]-graph[nr][nc])<=R:
                visited[nr][nc]=True
                que.append([nr, nc])
                union_.append([nr,nc])
                total+=graph[nr][nc]
                
    # 자기 자신 외 연합 존재하는 경우    
    if len(union_)>1:
        setUnion(union_, total)
        return 1
    else:
        return 0


def setUnion(union_, total):
    value = int(total/len(union_))
    for r,c in union_:
        graph[r][c]=value
        
answer=0

while answer<=2000:
    flag = 0 # 연합 존재여부
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not(visited[i][j]):
                # 단 한번이라도 연합 생긴 경우 flag는 0이 아님
                flag = max(flag, findUnion(i,j))
                
    if flag == 0:
        print(answer)
        break
    else:
        answer+=1
            