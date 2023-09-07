# day18: 대체 경로
import sys
input = sys.stdin.readline
from heapq import heappush, heappop # 최소힙
# N 개 도시(1-indexing), M개 도로
# s번 도시 -> e번 도시 이동
n, m ,start, end=map(int, input().split())
graph = [[] for _ in range(n+1)]



for _ in range(m):
	a,b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
	
	

	
# i일 뒤 i번 도시 공사 -> 연결된 것 모두 사용 불가능
# 출발 도시와 도착 도시에서 공사
# 두 도시 사이 이동 불가능

def search(i):
	if i==start or i==end:
		return -1
	count=1
	heap = []
	visited = [0]*(n+1)
	flag = False
	heappush(heap, [count,start])
	visited[start] = True
	while heap:
		count,node = heappop(heap)
		#print("pop", node)
		if node ==i:
			continue
		for nextNode in graph[node]:
			if not visited[nextNode] and nextNode!=i:
				visited[nextNode]=True
				heappush(heap,[count+1, nextNode])
				#print("node: ",node,"nextNode",nextNode,"count: ",count,graph[node])
				if nextNode == end:
					flag = True
					return count+1
			
	
	if not flag:
		return -1

	
for i in range(1, n+1):
	#print("======",i)
	print(search(i))
	#print("======")