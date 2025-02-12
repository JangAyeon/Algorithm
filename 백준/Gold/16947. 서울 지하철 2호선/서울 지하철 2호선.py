import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
cycle = [3000] * (n + 1) # 사이클까지 각 노드의 도달 거리
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n + 1)
finded = 0
def find_cycle(d, cnt): # 지나온 노드, 깊이
    global finded
    if finded: # 발견한 경우 시간 단축을 위해 중단
        return
    # 현재 노드와 연결된 노드 탐색
    for i in graph[d[-1]]: 
        if i == d[0] and cnt >= 2: # 사이클인 경우 종료
            for j in d:
                cycle[j] = 0 # j노드는 사이클에 속하는 노드
            finded = 1
            return
        if not visited[i]:
            visited[i] = 1
            find_cycle(d + [i], cnt + 1)
            visited[i] = 0

for i in range(1, n + 1):
    visited[i] = 1
    find_cycle([i], 0)
    visited[i] = 0

# 사이클에 속하는 노드로부터 BFS탐색
from collections import deque
q = deque()
for i in range(1, n + 1): 
    if cycle[i] == 0:
        q.append((i, 0))
while q:
    now, d = q.popleft()
    for v in graph[now]:
        if cycle[v] == 3000: # 방문하지 않은 경우 거리 기록
            cycle[v] = d + 1
            q.append((v, d + 1))
print(*cycle[1:])