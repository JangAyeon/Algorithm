"""
프림 알고리즘
1. 임의의 정점을 선택해 최소 신장 트리에 추가
2. 최소 신장 트리에 포함된 정점과 최소 신장 트리에 포함되지 않은 정점을 
연결하는 간선 중 비용이 가장 작은 것을 최소 신장 트리에 추가
3. 최소 신장 트리에 v-1개 간선이 추가될 때까지 2번 반복
"""

"""
프림 알고리즘 -  우선 순위 큐
1. 임의의 정점을 선택해 최소 신장 트리에 추가
2. 해당 정점과 연결된 모든 간선을 우선 순위 큐에 추가
3-1. 만약 해당 간선이 최소 신장 트리에 포함된 두 정점을 연결한다면 아무것도 하지 않고 넘어감
3-2. 해당 간선이 최소 신장 트리에 포함된 정점 u와 포함되지 않는 정점 v를 연결한다면 
해당 간선과 정점 v를 최소 신장 트리에 추가 후 정점 v과 최소 신장 트리에 포함되지 않는 모든 간선을 우선 순위 큐에 추가
4. 최소 신장 트리에 v-1개 간선이 추가될 때까지 2,3 과정 반복

"""
import sys
input = sys.stdin.readline
import heapq

n  = int(input())
arr = [int(input()) for _ in range(n)]
graph = [[] for _ in range(n+1)]
matrix = [[] for _ in range(n+1)]

for i in range(n):
    graph[0].append((arr[i],i+1))
for i in range(1,n+1):
    nodes = [0]+list(map(int, input().split()))
    matrix[i] = nodes
    
for i in range(1,n):
    for j in range(i+1, n+1):
        graph[i].append((matrix[i][j],j))
        graph[j].append((matrix[i][j],i))
        
visited = [True]+[False]*(n)
q = graph[0]
heapq.heapify(q)
result = 0
cnt = 0

while q:
    if cnt==n:
        break
    z,x = heapq.heappop(q)
    if not visited[x]:
        visited[x]=True
        cnt+=1
        result+=z
        for j in graph[x]:
            if not visited[j[1]]:
                heapq.heappush(q,j)

print(result)
