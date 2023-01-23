import sys
input= sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
from collections import deque

m,n = map(int, input().split()) # m : 세로, n:가로
graph = [list(map(int, input().split())) for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
dp = [[-1] * n for i in range(m)] #방문여부 확인

#print(n,m,graph)
'''
전체 문제가 최적의 해로 쪼갤 수 있는가?
도착지점까지 가는 경우의 수 =  임의의 점에서 도착지점까지 가는 경우의 수의 합
'''

def bfs(x,y):
    if x == m-1 and y == n-1: #base(기저)인 경우 
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i] #상하좌우 이동
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n: #이동해도 범위 내 존재함
                if graph[x][y] > graph[nx][ny]:
                        dp[x][y] += bfs(nx, ny) #도착지점에서 출발 지점까지 역순으로 경우의 수 추가 
    return dp[x][y]



print(bfs(0,0))