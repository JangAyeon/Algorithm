# https://what-am-i.tistory.com/m/77


import sys
input = sys.stdin.readline
from collections import deque 

## 입력받기

n = int(input()) # 그래프 생성
graph = [[0]*n for _ in range(n)]

m = int(input()) # 그래프에 사과 심기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1 

k = int(input()) # 회전
cmd = {}
for _ in range(k):
    x, c = input().split()
    cmd[int(x)] = c 



def change(d, c):
    # 상(0) 우(1) 하(2) 좌(3)
    # 동쪽 회전: 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) : +1 방향
    # 왼쪽 회전: 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0) : -1 방향
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]



def solution():
    direction = 1  # 초기 방향 - 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치
    time = 1  # 시간
    x, y = 0, 0  # 초기 뱀 위치
    visited = deque([[x, y]])  # 방문 위치
    graph[x][y] = 2
    while True:
        x, y = x + dx[direction], y + dy[direction]
        print("n",x,y)
        if 0 <= y < n and 0 <= x < n and graph[x][y] != 2:
            if not graph[x][y] == 1:  # 사과가 없는 경우
                temp_x, temp_y = visited.popleft()
                graph[temp_x][temp_y] = 0  # 꼬리 제거
            graph[x][y] = 2
            visited.append([x, y])
            if time in cmd.keys():
                direction = change(direction, cmd[time])
            time += 1
        else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
            return time

print(solution())