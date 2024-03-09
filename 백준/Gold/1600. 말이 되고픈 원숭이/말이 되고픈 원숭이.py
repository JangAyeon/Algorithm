import sys
input = sys.stdin.readline

from collections import deque

k = int(input())
m,n = map(int, input().split())
graph= [list(map(int, input().split())) for _ in range(n)]



def isValid(nr, nc, break_):
    if not(0<=nr<n) or not(0<=nc<m) or distance[nr][nc][break_]!=0 or graph[nr][nc]==1:
        return False
    else:
        return True
## 브레이, 
distance=[[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
def bfs(r,c,k):
    que = deque([[r,c,0]])
    distance[r][c][0]=0
    while que:
        r,c,break_ = que.popleft()
        ## print(r,c, break_)
        if r==n-1 and c==m-1:
            return distance[r][c][break_]
        ## 일반 움직임
        for nr, nc in [(r-1,c),(r+1,c),(r,c+1),(r,c-1)]:
            ## 범위 밖인 경우, 이전에 방문한 경우, 벽인 경우
            if not(isValid(nr, nc, break_)):
                continue
            distance[nr][nc][break_]=distance[r][c][break_]+1
            que.append([nr, nc,  break_])
        ## 말 움직임
        if break_<k:
            for nr, nc in [(r-2,c-1),(r-2,c+1),(r-1,c-2),(r-1,c+2),
                  (r+1,c-2),(r+1,c+2),(r+2,c-1),(r+2,c+1)]:
                if not(isValid(nr, nc, break_+1)):
                    continue
                distance[nr][nc][break_+1]=distance[r][c][break_]+1
                que.append([nr, nc,  break_+1])
    return -1

print(bfs(0,0, k))
    
    