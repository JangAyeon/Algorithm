# 합승 택시 요금


INF = 40000000

def floyd(dist, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k]+dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]
                    
                    
def graph(n, fares):
    graph = [[INF for _ in range(n)] for _ in range(n)] 
    
    for i in range(n):
        graph[i][i]=0
    
    for edges in fares:
        graph[edges[0]-1][edges[1]-1] = edges[2]
        graph[edges[1]-1][edges[0]-1] = edges[2]
    return graph

def solution(n, s, a, b, fares):
    
    ## 그래프 생성
    dist = graph(n, fares)
        
    ## 구간 간의 최소값 구하기
    floyd(dist, n)
    
    s-=1 # 0 indexing
    a-=1 # 0 indexing
    b-=1 # 0 indexing
    answer = INF
    for k in range(n): ## 합승 끝나는 구간
        answer = min(answer, dist[s][k]+dist[k][a]+dist[k][b])
    return answer