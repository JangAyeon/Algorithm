import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]


directions = [[(+1,0),(0,-1)],
[(-1,0),(0,-1)],
[(-1,0),(0,+1)],
[(+1,0),(0,+1)]]

def isAbleArea(r,c, direction):
    (dr1,dc1),(dr2,dc2)=direction
    nr1 = dr1+r
    nc1 = dc1+c
    nr2 = dr2+r
    nc2 = dc2+c
    if not(0<=nr1<n) or not(0<=nr2<n):
        ##print("Row",nr1, nr2)
        return False
    if not(0<=nc1<m) or not(0<=nc2<m):
        ##print("Col",nc1, nc2)
        return False
    if visited[r][c] or visited[nr1][nc1] or visited[nr2][nc2]:
        return False
    return True

answer = 0 
def dfs(r,c,total):
    global answer
    ##print("==================")
    
    ##for i in visited:
    ##    print(*i)
    if c==m:
        c,r=0,r+1
    if r==n:
        answer = max(answer, total)
        return
    ##print(r,c, total)
    if not(visited[r][c]):
        for direction in directions:
            if isAbleArea(r,c,direction):
                (dr1,dc1),(dr2,dc2)=direction
                sum_ = graph[r][c]*2+graph[r+dr1][c+dc1]+graph[r+dr2][c+dc2]
                visited[r][c]=visited[r+dr1][c+dc1]=visited[r+dr2][c+dc2]=True
                dfs(r,c+1,total+sum_)
                visited[r][c]=visited[r+dr1][c+dc1]=visited[r+dr2][c+dc2]=False
    dfs(r,c+1,total)

if n<2 and m<2:
    print(0)
else:

    dfs(0,0,0)
    print( answer)