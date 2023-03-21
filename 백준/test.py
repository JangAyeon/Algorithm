from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[0]*n for _ in range(n)] # 그래프 초기화
k = int(input())
for _ in range(k):
    i,j =map(int, input().split())
    graph[i-1][j-1]=1 # 사과 존재
m = int(input())
times={}
for _ in range(m):
    time, direction = input().split()
    times[int(time)]=direction


def rotation(direction,cmd):
    if cmd == "L":
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    print(cmd, direction)
    return direction


dx = [-1, 0, 1, 0]
dy = [0,1, 0, -1]
# 2: 방문, 1: 사과존재, 0: 꼬리자르기 - 방문 안함
def solution():
    direction = 1  # 초기 방향 - 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치
    time = 1  # 시간
    x, y = 0, 0  # 초기 뱀 위치
    visited = deque([[x, y]])  # 방문 위치
    graph[x][y] = 2
    while True:
        x, y = x + dx[direction], y + dy[direction]
        if 0 <= y < n and 0 <= x < n and graph[x][y] != 2:
            if not graph[x][y] == 1:  # 사과가 없는 경우
                temp_x, temp_y = visited.popleft()
                graph[temp_x][temp_y] = 0  # 꼬리 제거
            graph[x][y] = 2
            visited.append([x, y])
            if time in times.keys():
                direction = rotation(direction, times[time])
            time += 1
        else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
            return time



print(solution())