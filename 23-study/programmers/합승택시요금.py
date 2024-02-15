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
    
    
input1 = [6,4,6,2, 
    [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], 
    [2, 4, 66], [2, 3, 22], [1, 6, 25]]
]
input2 = [7,3,4,1,
[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
]
input3 = [6,4,5,6,
[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
]
inputs= [input1, input2, input3]

for n,s,a,b, fares in inputs:
    print(solution(n,s,a,b, fares))
    