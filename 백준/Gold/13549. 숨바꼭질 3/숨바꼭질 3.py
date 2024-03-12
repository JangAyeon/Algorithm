import sys
input = sys.stdin.readline
from collections import deque
#  1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X

n,m = map(int, input().split())
INF = float("inf")
distance = [INF for _ in range(100001)]
answer = INF

def bfs(start):
    que = deque([[start, 0]])
    global answer
    while que:
        now, time = que.popleft()
        if now == m:
            answer =min(answer, time)

        for idx,next_ in enumerate([now*2, now+1, now-1]):
            if 0<=next_<100001 and distance[next_]>time:
                distance[next_] = time if idx==0 else time+1
                que.append([next_, distance[next_]])
       

bfs(n)
print(answer)