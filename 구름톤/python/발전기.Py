import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
#visited = [[False]*(n) for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(r,c):
	que = deque()
	que.append([r,c])
	graph[r][c]=0
	while que:
		r,c = que.popleft()
		for i in range(4):
			nr, nc = r+ dr[i], c+dc[i]
			if not(0<=nr<n and 0<=nc<n):
				continue
			if graph[nr][nc]==1:
				que.append([nr, nc])
				graph[nr][nc]=0
	#print("===========")
	#for i in graph:
	#	print(*i)
	#print("===========")
			
answer = 0
for r in range(n):
	for c in range(n):
		if graph[r][c]==1:
			answer+=1
			bfs(r,c)
print(answer)