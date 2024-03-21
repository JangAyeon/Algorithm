## https://www.acmicpc.net/problem/7562

import sys
input = sys.stdin.readline
from collections import deque

dr=[-1,-2,-2,-1, +1, +2, +2, +1]
dc=[-2,-1,+1,+2, -2,-1, +1, +2 ]

def bfs(sr, sc, n):
    graph = [[-1 for _ in range(n)] for _ in range(n)]
    que = deque()
    que.append([sr, sc])
    graph[sr][sc]=0
    while que:
        r,c = que.popleft()
        for idx in range(len(dr)):
            nr, nc = r+dr[idx], c+dc[idx]
            if (not(0<=nr<n) or not(0<=nc<n) or graph[nr][nc]!=-1):
                continue
            graph[nr][nc] = graph[r][c]+1
            que.append([nr,nc])
            
    print(graph[er][ec])


T = int(input())

for _ in range(T):
    n = int(input())
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())

    bfs(sr, sc, n)
