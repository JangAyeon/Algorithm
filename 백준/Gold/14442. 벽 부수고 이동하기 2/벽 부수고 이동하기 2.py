import sys
from collections import deque

input = sys.stdin.readline
N,M,K = map(int, input().split(" "))
arr = [list(map(int, input().strip())) for _ in range(N)]

directions = [
    [-1,0],[1,0],
    [0,-1],[0,1]
]
visited = [[[0 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]


def bfs(r,c):
    que = deque()
    que.append([r,c,0])## r, c, 부순 횟수
    visited[r][c][0]=1
    while que:
        r,c, broken = que.popleft()
        if (r == N-1) and (c==M-1):
            return visited[r][c][broken]
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            ## 범위 벗어남
            if not(0<=nr<N) or not(0<=nc<M):
                continue
            ## print(nr,nc, broken)
            if arr[nr][nc]==0 and visited[nr][nc][broken]==0:
                visited[nr][nc][broken]=visited[r][c][broken]+1
                que.append([nr, nc, broken])
            elif arr[nr][nc]==1 and broken<K and visited[nr][nc][broken+1]==0:
                visited[nr][nc][broken+1] = visited[r][c][broken]+1
                que.append([nr, nc, broken+1])
    return -1
print(bfs(0,0))
            