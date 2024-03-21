## 반례 모음: https://www.acmicpc.net/board/view/119335

from collections import deque
import sys

input = sys.stdin.readline
#  N개의 줄에 M개의 숫자로 맵
n,m = map(int, input().split())
visited = [[[0,0] for _ in range(m)] for _ in range(n)]
dr,dc = [-1,1,0,0],[0,0,-1,1]
graph = []
#(1, 1)과 (N, M)은 항상 0이라고 가정
visited[0][0][0]=1

for _ in range(n):
    graph.append(list(map(int, input().strip())))



def bfs():
    que = deque()
    que.append((0,0,0))
    
    while que:
        r,c,break_ = que.popleft()
        for idx in range(4):
            if r ==n-1 and c==m-1:
                return visited[r][c][break_]
                
            nr, nc = r+dr[idx], c+dc[idx]
            ## 범위 아닌 경우 : 그냥 넘어가기
            if not(0<=nr<n) or not(0<=nc<m):
                continue
            ## 벽임 & 아직 벽 파괴 쓴 적 없음
            if graph[nr][nc] and break_==0:
                visited[nr][nc][1] = visited[r][c][0]+1
                que.append((nr, nc, 1))
            ## 벽 아님 & 방문한 적 없음 & 벽 파괴 여부 따질 필요 없음
            elif not(graph[nr][nc]) and not(visited[nr][nc][break_]):
                visited[nr][nc][break_]=visited[r][c][break_]+1
                que.append((nr,nc,break_))

    return -1






print(bfs())

