import sys
input = sys.stdin.readline
from heapq import heappop, heappush


    


while True:
    ## 집의 수 m과 길의 수 n
    m,n = map(int, input().split())
    if (m,n)==(0,0):
        break
    else:
            ## n개 줄
        ## x번 집 = y번 집 (양방향) => z미터
        
        
        graph = [[] for _ in range(m)]
        
        total=0
        for _ in range(n):
            a,b,cost = map(int, input().split())
            graph[a].append([b,cost])
            graph[b].append([a,cost])
            total+=cost
        
    

        costs = 0
        visited = [False]*(m)
        heapq = []
        start = 0
        heappush(heapq, [0, start])
        while heapq:
            cost, now = heappop(heapq)
            if visited[now]:
                continue
            costs+=cost
            visited[now]=True
            for next_node, next_cost in graph[now]:
                if not(visited[next_node]):
                    heappush(heapq, [next_cost, next_node])
                    

        
        print(total-costs)
        
   