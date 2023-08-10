import sys
import heapq 
input = sys.stdin.readline
INF = sys.maxsize

# 정점갯수, 간선 갯수 
n,m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
q = []

for _ in range(m):
    s,e,c  = map(int, input().split())
    graph[s].append((e,c)) # 목적지 노드, 가중치 
    
    
def dijkstra(start):
    heapq.heappush(q,(0, start)) # 거리, 노드 번호
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for  next_node, weight in graph[now]:
            cost = dist + weight
            if distance[next_node]>cost:
                distance[next_node] = cost
                heapq.heappush(q,(cost,next_node))
                
dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])