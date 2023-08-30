# day 13: 발전기2

import sys
input = sys.stdin.readline
from collections import deque

n,k  =map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]
build = {}

def bfs(r,c, t):
	que = deque()
	que.append([r,c])
	graph[r][c] = 0 #방문처리 
	count=1
	while que:
		r, c = 	que.popleft()
		for idx in range(4):
			nr, nc = r + dr[idx], c + dc[idx]
			if not(0<=nr<n and 0<=nc<n):
				continue
			#print(nr,nc, t, graph[nr][nc])
			if graph[nr][nc]==t:
				que.append([nr,nc])
				count+=1
				graph[nr][nc] = 0
				
	if count>=k:
		if t in list(build.keys()):
			build[t]+=1
		else:
			build[t] = 1
			
for i in range(n):
	for j in range(n):
		if graph[i][j]!=0:
			bfs(i, j, graph[i][j])
			
answer = [k for k,v in build.items() if max(build.values()) == v]
# 건물이 여러 개면 유형 번호가 더 큰 것
print(max(answer))