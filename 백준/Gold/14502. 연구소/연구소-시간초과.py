# 깊은 객체 복사 + 재귀 등의 사용으로 시간 초과 발생
# 파이썬: 시간초과, pypy3 통과 코드

import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]
# 0은 빈 칸, 1은 벽, 2는 바이러스
dr = [-1,1,0,0]
dc = [0,0,-1,1]
answer = 0
# 어디에 벽을 세울 수 있을지 모르기 때문에
# 모든 경우의 수 수행
# 백트레킹으로 벽 세우고 벽 지우는 방식 반복

def make_wall(count):
    if count == 3:
        bfs()
        return
    
    for i in range(row):
        for j in range(col):
            # 빈칸인 경우 벽 세우기
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count+1)
                graph[i][j]=0

def bfs():
    que = deque()
    temp_graph = deepcopy(graph)
    for i in range(row):
        for j in range(col):
            if temp_graph[i][j]==2:
                que.append([i,j])
    
    while que:
        r,c = que.popleft()
        for idx in range(4):
            nr,nc = r +dr[idx], c + dc[idx]
            if not(0<=nr<row and 0<=nc<col):
                continue
            if temp_graph[nr][nc] ==0:
                temp_graph[nr][nc] = 2
                que.append([nr, nc])
                
    global answer
    #print("============")
    #print(graph)
    cnt = 0
    
    for i in range(row):
        for j in range(col):
            if temp_graph[i][j]==0:
                cnt+=1
    answer = max(answer, cnt)
            
make_wall(0)    
print(answer)
