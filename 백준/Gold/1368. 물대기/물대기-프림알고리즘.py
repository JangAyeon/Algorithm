
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
        # start, cost, end
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
        for j in graph[x]: # 연결된 end 노드 방문한 적 없는 경우
            if not visited[j[1]]:
                heapq.heappush(q,j)

print(result)
