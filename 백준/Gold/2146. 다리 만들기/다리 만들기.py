import sys
input = sys.stdin.readline
from collections import deque


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]



visited = [[False]*(n) for _ in range(n)]
## 영역 번호 부여
def area(r,c, landIdx):
    que = deque([[r,c]])
    visited[r][c]=True
    graph[r][c]=landIdx
    while que:
        r,c = que.popleft()
        for nr, nc in [(r-1, c),(r+1, c),(r,c-1),(r,c+1)]:
            ## 범위 내 아닌 경우, 방문한 경우, 바다인경우:
            if not(0<=nr<n) or not(0<=nc<n) or visited[nr][nc]==True or graph[nr][nc]==0:
                continue
            visited[nr][nc]=True
            graph[nr][nc]=landIdx
            que.append([nr,nc])


## 영역 연결 하기
def connect(r,c, landIdx):
    que = deque([[r,c, 0]])
    visited2[r][c]=True
    ## print(r,c)
    while que:
        r,c, count =que.popleft()

        ## 조기 종료 조건 : 다른 영역 도착한 경우 && 바다가 아닌 경우
        if graph[r][c]!=landIdx and graph[r][c]!=0:
            ## print("return", count, r,c, graph[r][c], landIdx)
            return count
        for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            ## 범위 아닌 경우, 이미 방문한 경우
            if not(0<=nr<n) or not(0<=nc<n) or (visited2[nr][nc]==True):
                continue
            visited2[nr][nc]=True
            ## 바다에 다리 놓는 경우
            if graph[nr][nc]==0:
                ## print(nr, nc, graph[nr][nc], count)
                que.append([nr,nc, count+1])
            else:
                que.append([nr, nc,count])
    return float("inf")


                

landIdx = 0
for r in range(n):
    for c in range(n):
        if visited[r][c]==False and graph[r][c]==1:
            landIdx+=1
            area(r,c, landIdx)



answer = float("inf")
for land in range(1, landIdx+1):
    visited2 = [[False]*(n) for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if graph[r][c]==land and visited2[r][c]==False:
                
                answer = min(answer,connect(r,c, land))

                
print(answer)






