from collections import deque

# N개 마을, M개 단방향 도로, X번 마을에서 파티 
# 1-indexing
n,m,x =  map(int, input().split())
graph = [[] for _ in range(n+1)]
# 시작점, 끝점, 소요시간
for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start].append([end, time])
INF = 1e9

def djsktra(start):
    distance=[INF]*(n+1)
    que = deque()
    distance[start] = 0
    que.append([start, distance[start]])
    
    while que:
        currNode, currDist = que.popleft()
        for nextNode, cost in graph[currNode]:
            #print(start, currNode, nextNode, cost, currDist)
            if distance[nextNode]>cost+ currDist:
                distance[nextNode] = cost+currDist
                que.append([nextNode, distance[nextNode]])
    return distance
towns = [i for i in range(1, n+1)]
towns.remove(x)

back = djsktra(x)
answer = -INF
for start in towns:
    answer = max(answer,djsktra(start)[x]+ back[start])
print(answer)