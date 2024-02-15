import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = list([0]*n for _ in range(n)) # 그래프 (0:방문 X, 1 : 사과, 2: 방문)
k = int(input())
for _ in range(k): # 사과 입력 받기
    i,j= map(int, input().split())
    graph[i-1][j-1]=1 

l = int(input())
times = {}
for _ in range(l):
    time, cmd = input().split()
    times[int(time)] = cmd # 명령어


dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]

def rotation(direction, cmd):
    if cmd == "L":
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction

def solution():
    direction = 1  # 초기 방향 - 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치
    time = 1  # 시간
    x, y = 0, 0  # 초기 뱀 위치
    visited = deque([[x, y]])  # 방문 위치
    graph[x][y] = 2

    while True:
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= ny < n and 0 <= nx < n and graph[nx][ny] != 2:
            if graph[nx][ny] != 1:  # 사과가 없는 경우
                temp_x, temp_y = visited.popleft()
                graph[temp_x][temp_y] = 0  # 꼬리 제거
            graph[nx][ny] = 2
            visited.append([nx, ny])
            if time in times.keys():
                direction = rotation(direction, times[time])
            time += 1
            x,y=nx,ny
        else:
            return time


print(solution())