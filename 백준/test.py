## https://www.acmicpc.net/problem/1697

import sys
from collections import deque

a,b = map(int, sys.stdin.readline().split())
MAX = 100000
visited = [0]*(MAX+1)

def bfs(a):
    que = deque([a])
    while que:
        x = que.popleft()
        if x == b:
            print(visited[x])
            return
        for dx in (x-1,x+1,x*2):
            if 0<= dx <=MAX and not visited[dx]:
                que.append(dx)
                visited[dx] = visited[x]+1




bfs(a)
