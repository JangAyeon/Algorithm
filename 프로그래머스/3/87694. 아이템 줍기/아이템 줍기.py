from collections import deque



def bfs(start, end, graph):
    n = len(graph)
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    
    que = deque([start])
    while que:
        r, c = que.popleft()
        if [r,c]==end:
            return graph[r][c]//2
        for idx in range(4):
            nr, nc = r + dr[idx], c+dc[idx]
            ## 범위 나가는 경우
            ## 1) 그래프 밖에 2) 도형 영역 밖에 3) 도형 영역 안에
            if not(0<=nr<n and 0<=nc<n) or graph[nr][nc]==0 or graph[nr][nc]==-1:
                continue
            ## 최초로 방문한 경우
            if graph[nr][nc]==1:
                graph[nr][nc]= graph[r][c]+1
                que.append([nr, nc])

    
    


def makeGraph(c1,r1,c2,r2, graph):
    for r in range(r1, r2+1):
        for c in range(c1,c2+1):
            ## 테두리 좌표 && 다른 도형의 안쪽 아님 
            if (r1==r or r==r2 or c1==c or c==c2) and graph[r][c]!=0:
                graph[r][c]=1
            else:
                graph[r][c]=0
    return graph
    


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    ## rectangle = [[1,1,7,4],[3,2,5,5]]
    n=102
    graph = [[-1]*(n) for _ in range(n)]
    
    
    for c1,r1,c2,r2 in rectangle:
        graph =makeGraph(2*c1,2*r1,2*c2,2*r2, graph)
        
    answer = (bfs( [2*characterY,2*characterX],[2*itemY,2*itemX], graph))
        
        
    return answer