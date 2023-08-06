
import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(input().strip()) for _ in range(row)]
j_visited = [[0]*col for _ in range(row)]
f_visited = [[0]*col for _ in range(row)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

f_que = deque()
j_que = deque()


def fire_bfs():
    while f_que:
        x, y = f_que.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            #범위 밖에 있는 경우 // 벽인 경우 // 불이 이전에 방문한 경우
            if not(0<=nx<row and 0<=ny<col) or graph[nx][ny]=="#" or f_visited[nx][ny]:
                continue
            #최초방문인 경우 : 기준점 + 1, 탐색 추가
            f_visited[nx][ny] = f_visited[x][y]+1
            f_que.append([nx, ny])
  


def jh_bfs():
    while j_que:
        x, y = j_que.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            #범위 밖으로 도달 - 탈출한 경우
            if not(0<=nx<row and 0<=ny<col):
                print(j_visited[x][y])
                return
            # 벽인 경우 // 지훈이 이전에 방문한 경우
            if graph[nx][ny]=="#" or j_visited[nx][ny]:
                continue
            # 불이 도달한 적이 없거나 불보다 먼저 칸에 도착한 경우 - 방문 가능인 경우
            if not(f_visited[nx][ny]) or f_visited[nx][ny]>j_visited[x][y]+1:
                j_visited[nx][ny] = j_visited[x][y]+1
                j_que.append([nx, ny])
    print("IMPOSSIBLE")
 
# BFS 돌기
for i in range(row):
    for j in range(col):
        #print(i,j, graph[i][j])
        if graph[i][j]=="F":
            f_visited[i][j]=True
            f_que.append([i,j])
        elif graph[i][j] == "J":
            j_visited[i][j] = 1 
            j_que.append([i,j])
fire_bfs()
jh_bfs()
