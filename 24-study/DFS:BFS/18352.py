## 1번 ~ N번까지 도시
## M개 단방향
## 최단거리 K
## 출발도시 X
## 이미 제시한 최단 거리이면 더이상 거리 따질 필요 없음

import sys
input = sys.stdin.readline
from collections import deque

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = float("inf")
dist = [INF for _ in range(n+1)] ## INF이면 최초 방문임
dist[x]=0
answer = []
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    


def bfs(start):
    que = deque()
    que.append(start)
    while que:
        curr = que.popleft()
        if dist[curr]==k: ## 이미 최단 거리임
            answer.append(curr)
            continue
        for next_ in graph[curr]:
            ## print("curr", curr, dist)
            if dist[next_]>dist[curr]+1:
                dist[next_]=dist[curr]+1
                que.append(next_)

bfs(x)
answer = answer if len(answer) else [-1]
answer.sort() #deque에서 pop한 게 꼭 정렬순 아닐 수 잇음
for v in answer:
    print(v)
    
    