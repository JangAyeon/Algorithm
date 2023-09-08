# day20: 연결 요소 제거하기

import sys
input = sys.stdin.readline
from collections import deque

# 배열 크기, 연결요소 지우는 기준, 문자 적는 횟수
n,k,q = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
#print(graph)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1] 

def clear(spots):
	for r,c in spots:
		graph[r][c]="."

def bfs(r, c):
	que = deque()
	que.append([r,c])
	lst = [[r,c]]
	ch = graph[r][c]
	visited=[[False]*(n+1) for _ in range(n+1)]
	visited[r][c]=True
	#print(visited[r][c])
	while que:
		row,col = que.popleft()
		for idx in range(4):
			nr, nc = row + dr[idx], col + dc[idx]
			if not(0<=nr<n and 0<=nc<n) or graph[nr][nc]!=ch:
				continue
			if not visited[nr][nc] and graph[nr][nc]==ch:
				que.append([nr,nc])
				lst.append([nr, nc])
				visited[nr][nc]=True
	if len(lst)>=k:
		clear(lst)


		

for _ in range(q):
	row, col, ch = input().strip().split()
	row, col = int(row)-1,int(col)-1
	graph[row][col]=ch
	bfs(row, col)
	
	#print("================", row, col, ch)
for i in graph:
	print(*i, sep="")
	