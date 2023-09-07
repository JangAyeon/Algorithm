# 문제 16. 연합

## 유니온 파인드 활용 
import sys
input = sys.stdin.readline

INF = int(1e9)
# 섬의 갯수, 다리갯수
n,m = map(int, input().split())
parent = [i  for i in range(n+1)]
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
	start, end = map(int, input().split())
	graph[start][end]=1
	
def findParent(parent, node):
	if parent[node]!=node:
		parent[node] = findParent(parent, parent[node])
	return parent[node]

def findUnion(parent, a,b):
	a = findParent(parent, a)
	b = findParent(parent, b)
	
	if a<b:
		parent[b] = a
		
	elif b<a:
		parent[a]=b
	

	

for i in range(1, n+1):
	for j in range(1,n+1):
		if graph[i][j]==1 and graph[j][i]==1:
			findUnion(parent, i,j)

answer = set()
for i in range(1,n+1):
	answer.add(findParent(parent,i))
	
		
print(len(answer))





## BFS 이용
import sys
input = sys.stdin.readline
from collections import deque
# 섬의 갯수, 다리갯수
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1) # BFS를 위한 방문 배열
result = 0


for _ in range(m):
	start, end = map(int, input().split())
	graph[start].append(end) # 단방향으로 이동
	
for i in range(1, n+1):
	if visited[i]:
		continue
	que = deque([i])
	result+=1
	visited[i]=True
	while que:
		node = que.popleft()
		for nextNode in graph[node]:
			# 두 섬은 서로 이동할 수 있어야 함
			# 가는 간선과 오는 간선이 동시에 존재
			if not visited[nextNode] and node in graph[nextNode]:
				que.append(nextNode)
				visited[nextNode]=True
print(result)