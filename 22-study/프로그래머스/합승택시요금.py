INF = 40000000

def floyd(n, graph):
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k]+graph[k][j]:
                    graph[i][j] = graph[i][k]+graph[k][j]


def drawGraph(n, fares):
    graph = [[INF for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        graph[i][i]=0
    
    for c, d, f in fares:
        graph[c-1][d-1]=graph[d-1][c-1]=f
    
    return graph

def solution(n, s, a, b, fares):
    graph = drawGraph(n,fares)
    floyd(n,graph)
    
    a-=1
    b-=1
    s-=1
    answer = INF
    for c in range(n):
        answer = min(answer, graph[s][c]+graph[c][b]+graph[c][a])
    
    return answer