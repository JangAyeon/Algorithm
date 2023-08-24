import sys
input = sys.stdin.readline
from collections import deque

# #: 폭탄 값 동일, 0: 폭탄 1증가, @: 폭탄 2 증가

n, k = map(int, input().split())
graph = [input().split() for _ in range(n)]
bomb = [[0 for _ in range(n)] for _ in range(n)]
dr = [0,-1,1,0,0]
dc = [0,0,0,-1,1]
#print(bomb)

# 1-indexing
cmds = []
for _ in range(k):
	r, c = map(int, input().split())
	cmds.append([r-1, c-1]) # 0-indexing으로 변환
que = deque(cmds)

def bombSpread():
	while que:
		r, c = que.popleft()
		for idx in range(5):
			nr, nc = r + dr[idx], c + dc[idx]
			if not(0<=nr<n and 0<=nc<n):
				continue
			if graph[nr][nc]=="#":
				continue
			elif graph[nr][nc]=="@":
					bomb[nr][nc]+=2
			else:
				bomb[nr][nc]+=1		

					
bombSpread()


answer = 0
for i in bomb:
	answer = max(answer,max(i))

print(answer)		
