from collections import deque
import sys

input = sys.stdin.readline
#  N개의 줄에 M개의 숫자로 맵
n,m = map(int, input().split())
visited=[[[0,0] for _ in range(m)] for _ in range(n)]
graph = []
dr=[-1,1,0,0]
dc=[0,0,-1,1]
# print(visited)

for _ in range(n):
    graph.append(list(map(int, input().strip())))
#print(graph)


def bfs():
    ## 시작
    visited[0][0][0]=1
    que=deque()
    que.append((0,0,0))
    while que:
        r,c,break_ = que.popleft()
        if r==n-1 and c == m-1:
            return visited[r][c][break_]
        for idx in range(4):
            nr, nc = r + dr[idx], c+dc[idx]
            if not(0<=nr<n) or not(0<=nc<m): ## 방문 불가능한 범위
                continue
            ## 벽 아님 => 벽파괴 불필요 & 아직 방문 안함
            if graph[nr][nc]==0 and visited[nr][nc][break_]==0:
                visited[nr][nc][break_]=visited[r][c][break_]+1
                que.append((nr, nc, break_))
            ## 벽임 & 이전에 벽 파괴 사용한 경우 없어서 지금 사용 가능
            elif graph[nr][nc]==1 and break_==0:
                visited[nr][nc][1]=visited[r][c][break_]+1
                que.append((nr, nc, 1))
                
    return -1


print(bfs())
    
    