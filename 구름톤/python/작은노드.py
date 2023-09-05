# day14: 작은 노드 


## BFS : 인접 리스트 활용 
import sys
input = sys.stdin.readline
from collections import deque
# 노드 갯수, 간선 갯수, 시작 노드 번호
v, e, start = map(int, input().split())
graph = [[] for _ in range(v+1) ]
distance = [0]*(v+1)



for _ in range(e):
	a,b  = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
	
	
def game(start):
	lastNode = start
	distance[start]=1
	que = deque()
	que.append(start)
	while que:
		start = que.popleft()
		for node in sorted(graph[start]):
			if distance[node]==0:
				distance[node]=1
				lastNode = node
				que.append(node)
				break
	
	return lastNode
	
	
	
	
node = game(start)
print(sum(distance), node)


## DFS : 인접 리스트
import sys
sys.setrecursionlimit(10**4)


N, M, start = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
	s, e = map(int, input().split())
	graph[s].append(e)
	graph[e].append(s)

def dfs(now):
	for to in sorted(graph[now]):
		if not visited[to]:
			visited[to] = 1
			return dfs(to)
	else:
		return now



visited[start] = 1
result = dfs(start)
print(sum(visited), result)