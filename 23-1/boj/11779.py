import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = int(1e9)

v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)
pre_ = [0]*(v+1)
heap = []
route = []

# 그래프 초기화
for _ in range(e):
    s,e,c = map(int, input().split())
    # 목적지 노드, 가중치
    graph[s].append((e,c))

start, end = map(int, input().split())

def dijkstra(start):
    distance[start] = 0
    # 우선순위 : 거리/가중치, 노드 번호
    heappush(heap,(0,start))
    
    while heap:
        dist, now = heappop(heap)
        
        if distance[now]<dist:
            continue
        for next_node, weight in graph[now]:
            cost  = weight+dist
            if distance[next_node]>cost:
                distance[next_node] = cost
                # 어떤 노드를 타고 왔는지 pre_ 테이블에 기록
                pre_[next_node] = now
                heappush(heap,(cost, next_node))
                
dijkstra(start) 
print(distance[end])
while end!=0:
    route.append(end)
    end = pre_[end]

route.reverse()
print(len(route))
print(" ".join(map(str, route)))

