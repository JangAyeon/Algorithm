import sys
input = sys.stdin.readline
from collections import deque

n=int(input())
graph = [[0]*n for _ in range(n)] # 0 : 뱀 없음, 1 : 사과 있음, 2 : 방문

k = int(input())
for _ in range(k):
    a,b = map(int, input().split())
    graph[a-1][b-1]=1

l = int(input())
times = {}
for _ in range(l):
    a, b = input().split()
    times[int(a)]=b

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def rotation(direction, cmd):
    if cmd  == "D":
        direction = (direction+1)%4
    else:
        direction = (direction-1)%4
    return direction

def solution():
    direction = 1
    x, y = 0, 0
    graph[x][y]=2
    visited = deque([[x,y]])
    time = 1 

    while True:
        nx, ny = x + dx[direction], y + dy[direction]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=2:
            if graph[nx][ny]!=1: # 사과 없음
                temp_x, temp_y = visited.popleft()
                graph[temp_x][temp_y] = 0 # 자리빼기
            if time in times.keys():
                direction  = rotation(direction, times[time])
            graph[nx][ny]=2
            visited.append([nx,ny])
            time+=1
            x, y = nx, ny
        else:
            return time



print(solution())