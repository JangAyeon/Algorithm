INF=int(1e9)

def drawGraph(n, fares):
    graph = [[INF]*(n+1) for _ in range(n+1)]
    
    for row in range(1, n+1):
        for col in range(1, n+1):
            if row == col:
                graph[row][col] = 0
    for c, d, f in fares:
        graph[c][d]= graph[d][c]=f
        
    return graph
    
    
def floyd(graph,n):
    for mid in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                graph[start][end] = min(graph[start][end],graph[start][mid]+graph[mid][end])
    
    return graph
    
    
def taxi(f_graph,n, s, a, b):
    cost = INF
    for mid in range(1,n+1):
        #print(mid, f_graph[s][mid],f_graph[mid][a],f_graph[mid][b])
        cost = min(cost, f_graph[s][mid]+f_graph[mid][a]+f_graph[mid][b])
    return cost
    
def solution(n, s, a, b, fares):
    
    graph = drawGraph(n, fares)
    f_graph = floyd(graph,n)
    answer = taxi(f_graph, n, s, a,b)
    
    return answer
    
    
    