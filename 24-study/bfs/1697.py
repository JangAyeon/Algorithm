import sys
input = sys.stdin.readline
from collections import deque

## 이동: x+1, x-1, x*2

n,k = map(int, input().split())

INF = float("inf")
MAX = 100000
dist = [INF for _ in range(MAX+1)]
dist[n]=0

def loc(x):
    location = [x+1, x-1, x*2]
    location = [v for v in location if 0<=v<=MAX]

    return location

def bfs(start):
    que = deque()
    que.append(start)
    while que:
        curr = que.popleft()
        for next_ in loc(curr):
            if dist[next_]>dist[curr]+1:
                dist[next_]=dist[curr]+1
                que.append(next_)

bfs(n)
print(dist[k])