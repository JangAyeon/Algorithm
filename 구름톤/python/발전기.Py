import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
#visited = [[False]*(n) for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(r,c):
	# 시작 노드를 큐에 삽입하고 방문 처리(해당 칸 0으로 변경)
	que = deque()
	que.append([r,c])
	graph[r][c]=0
	while que:
		# 큐에서 해당 노드를 꺼내
		r,c = que.popleft()
		# 해당 노드의 인접 노드
		for i in range(4):
			nr, nc = r+ dr[i], c+dc[i]
			if not(0<=nr<n and 0<=nc<n):
				continue
			# 인접 노드 중 아직 방문하지 않은 노드(아직 해당 칸이 1이 아니라 0인 경우)를 
			if graph[nr][nc]==1:
				que.append([nr, nc]) # 큐에 추가하고
				graph[nr][nc]=0 # 방문 처리(해당 칸 0으로 변경)함
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


"""
## 일부 테스트 케이스 시간 초과 발생 코드 
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
#visited = [[False]*(n) for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(r,c):
	global answer
	que = deque()
	que.append([r,c])
	answer+=1
	while que:
		r,c = que.popleft()
		graph[r][c]=0
		for i in range(4):
			nr, nc = r+ dr[i], c+dc[i]
			if not(0<=nr<n and 0<=nc<n):
				continue
			if graph[nr][nc]==1:
				que.append([nr, nc])
	#print("===========")
	#for i in graph:
	#	print(*i)
	#print("===========")
			
answer = 0
for r in range(n):
	for c in range(n):
		if graph[r][c]==1 :
			bfs(r,c)
print(answer)

"""