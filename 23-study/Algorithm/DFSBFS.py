"""
[BFS]
너비 우선 탐색 (가까운 노드부터 탐색하는 알고리즘)

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 모든 노드를 큐에 삽입하고 방문 처리함
3. 2번 과정을 더이상 수행할 수 없는 때까지 반복함
"""


from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = True
    while que:
        v = que.popleft()
        print(v , end=" ")
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i]=True
            

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False]*9

dfs(graph, 1, visited)
bfs(graph, 1, visited)