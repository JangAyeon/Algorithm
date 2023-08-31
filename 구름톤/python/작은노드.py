# day14: 작은 노드 

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

