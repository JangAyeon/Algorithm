import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)
heap = []

# 그래프 초기화
for _ in range(e):
    s,e,c = map(int, input().split())
    # 목적지 노드, 가중치
    graph[s].append((e,c))


def dijkstra(start):
    distance[start] = 0
    # 우선순위 : cost, node
    heappush(heap,(0,start))
    
    while heap:
        dist, now = heappop(heap)
        
        if distance[now]<dist:
            continue
        for next_node, weight in graph[now]:
            cost  = weight+dist
            if distance[next_node]>cost:
                distance[next_node] = cost
                heappush(heap,(cost, next_node))
                
dijkstra(start) 

for i in range(1, v+1):
    if distance[i] ==INF:
        print("INF")
    else:
        print(distance[i])
