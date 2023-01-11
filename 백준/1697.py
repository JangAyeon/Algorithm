import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
MAX =  100000
visited = [0] * (MAX+1)

def bfs(a):
    que =  deque([a])
    while que:
        x = que.popleft()
        if x == m:
            print(visited[x])
            return 
        for dx in (x+1, x-1, x*2):
            if 0<= dx <=MAX and not visited[dx]:
                visited[dx]= visited[x]+1
                que.append(dx)

bfs(n)