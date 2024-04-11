import sys
input =  sys.stdin.readline
from heapq import heappop, heappush


## N, M, X, Y
N,M,X,Y = map(int, input().split())
graph = [[] for _ in range(N)]
heap= []


for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

## 해당 노드의 왕복 거리 저장
INF = float("inf")
distance = [INF]*(N)

distance[Y]=0
for node, cost in graph[Y]:
    distance[node]=cost*2
    heappush(heap,[cost*2, node])


while heap:
    dist, node = heappop(heap)
    for next_, cost in graph[node]:
        if distance[node]+2*cost<distance[next_]:
            distance[next_] = distance[node]+2*cost
            heappush(heap, [distance[next_], next_])

distance.sort()
## print(distance)
def getDay(distance):
    total = 0
    day = 1
    for v in distance:
        ## print(v,day,total)
        if total+v<=X:
            total+=v
        else:
            day+=1
            total=v
    ## print("##", day)
    return day

if distance[-1]>X:
    print(-1)
else:
    print(getDay(distance))




        

"""
5 6 21 0
0 1 6
0 2 3
0 3 10
1 2 2
2 4 7
3 4 8
"""