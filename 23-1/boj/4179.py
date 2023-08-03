import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(input().strip()) for _ in range(row)]
visited = [[-1]*col for _ in range(row)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

Fque = deque()
Jque = deque()

def isEscape(visited, graph):
    answer = []
    # 맨 위 줄, 맨 아래 줄 전제
    for i in [0, row-1]:
        for j in range(len(visited[i])):
            if graph[i][j]!="#" and visited[i][j]!=-1:
                answer.append(visited[i][j])
    
    # 중간 양 시작과 끝
    for i in range(1, row):
        for j in [0, col-1]:
            if graph[i][j]!="#" and visited[i][j]!=-1:
                answer.append(visited[i][j])
    return answer

def fire_bfs(que):
    while que:
        x, y = que.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            #범위 밖에 있는 경우
            if nx<0 or row<=nx or ny<0 or col<=ny or graph[nx][ny]=="#" or graph[nx][ny]=="J" or graph[nx][ny]=="F":
                continue
            #최초방문인 경우 : 기준점 + 1, 탐색 추가
            #print(graph[nx][ny])
            if graph[nx][ny]=="." or graph[nx][ny] > graph[x][y]+1:
                graph[nx][ny] = graph[x][y]+1
                que.append([nx, ny])
                
    

def jh_bfs(que):
    while que:
        x, y = que.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            #범위 밖에 있는 경우
            if nx<0 or row<=nx or ny<0 or col<=ny:
                continue
            #최초방문인 경우 : 기준점 + 1, 탐색 추가
            if graph[nx][ny]!="#" and visited[nx][ny]==-1:
                # 불이 방문 못한 . 인 곳
                # 불 도착전에 접근 가능한 경우
                if graph[nx][ny]=="." or visited[x][y]+1<graph[nx][ny]:
                    #print(nx, ny)
                    visited[nx][ny] = visited[x][y]+1
                    que.append([nx, ny])
                    
 
# BFS 돌기
for i in range(row):
    for j in range(col):
        #print(i,j, graph[i][j])
        if graph[i][j]=="F":
            graph[i][j] = 1  
            #print("fire")
            Fque.append([i,j])
        elif graph[i][j] == "J":
            visited[i][j] = 1 
            Jque.append([i,j])
fire_bfs(Fque)
jh_bfs(Jque)
escape = isEscape(visited, graph)


#print("graph")
#for i in graph:
#    print(i)
#print("visited")
#for i in visited:
#    print(i)
    
if not escape:
    print("IMPOSSIBLE")
else:
    print(min(escape))