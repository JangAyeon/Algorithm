import sys
#본 시험에서는 solution 코드와 별도로 필요한 함수만 작성합니다.

INF = 1e7 #최대 n-1개의 간선을 지나게 됨

def drawGraph(n,fares):
	graph = [[INF]*(n+1) for _ in range(n+1)]
	for row in range(1, n+1):
		for col in range(1, n+1):
			if row == col:
				graph[row][col] = 0
				
	for d,e,f in fares:
		graph[d][e] = graph[e][d] = f
		
	return graph

def floyd(n, graph):
	for mid in range(1, n+1):
		for row in range(1, n+1):
			for col in range(1, n+1):
				graph[row][col] = min(graph[row][col], graph[row][mid]+graph[mid][col])
	
	return graph

def taxi(n, s, a, b, lay, graph):
	answer = INF
	for mid in range(1,n+1):
		answer = min(answer,graph[s][lay]+graph[lay][mid]+graph[mid][a]+graph[mid][b])
		
	return answer

def solution(n, s, a, b, fares, lay):
#들여쓰기에 주의하면서 필요한 코드를 작성하세요
	graph = drawGraph(n, fares)
	f_graph = floyd(n,graph)
	answer = taxi(n,s,a,b, lay, graph)
	
	return answer