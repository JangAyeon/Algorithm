from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
graph=[list(input().strip()) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
F_que, J_que=deque(),deque()
F_visited,J_visited=[[0]*M for _ in range(N)],[[0]*M for _ in range(N)]
#print(N,M,graph,F_visited,J_visited)


def bfs():
    while F_que:
        x,y=F_que.popleft()
        for k in range(4):
            nx,ny=x+dx[k], y+dy[k]
            if 0<=nx<N and 0<ny<M:
                if graph[nx][ny]!="#" and not F_visited[nx][ny]:
                    F_visited[nx][ny]=F_visited[x][y]+1
                    F_que.append((nx,ny))
    while J_que:
        x,y=J_que.popleft()
        for k in range(4):
            nx,ny=x+dx[k], y+dy[k]
            if 0 <= nx < N and 0 <= ny < M:
            # if 0<=nx<N and 0<ny<M:
                 if not J_visited[nx][ny] and graph[nx][ny] != '#':
                  if not F_visited[nx][ny] or F_visited[nx][ny] > J_visited[x][y] + 1:   
                        J_visited[nx][ny] = J_visited[x][y] + 1
                        J_que.append((nx, ny))
            else:
                return J_visited[x][y]+1
    return "IMPOSSIBLE"

for i in range(N):
    for j in range(M):
        if graph[i][j]=="J":
            J_que.append((i,j))
        elif graph[i][j]=="F":
            F_que.append((i,j))

print(bfs())

#print(F_visited)
#print (J_visited)