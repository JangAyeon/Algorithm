import sys
input = sys.stdin.readline
from collections import deque

## 작업할 개수 N, 작업 순서 정보의 개수 M
N,M = map(int, input().split())

indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]
## A, B => A를 하고 나서 B 해야 함

for _ in range(M):
    a,b =map(int, input().split())
    graph[b].append(a)

q = int(input())
que =  deque()

for start in graph[q]:
    que.append(start)
    indegree[start]=1

while que:
    node = que.popleft()

    for next_ in graph[node]:
        if indegree[next_]:
            continue
        indegree[next_]=1
        que.append(next_)
print(sum(indegree))