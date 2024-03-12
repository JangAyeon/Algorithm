import sys
input = sys.stdin.readline
from collections import deque


n,m = map(int, input().split())
INF = float("inf")
distance = [INF for _ in range(100001)]
answer = INF

def bfs(start):
    que = deque()
    que.append(start)
    distance[start] = 0
    while que:
        now = que.popleft()
        if now == m:
            return distance[now]
        for idx,next_ in enumerate([now*2, now+1, now-1]):
            dist =  distance[now] if idx==0 else distance[now]+1
            if 0<=next_<100001 and distance[next_]>dist:
                #  1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X
                distance[next_] =dist
                que.append(next_)
       

print(bfs(n))
