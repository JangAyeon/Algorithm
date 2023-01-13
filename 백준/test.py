from collections import deque 

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
dx = [0,0,-1, 1]
dy = [-1, 1, 0, 0]

ans = []

def bfs(graph, a, b):
    graph[a][b]=0
    cnt = 1
    #queue = deque().append((a,b)) : 오류 발생함 이렇게 짜면 안 됨
    que = deque()
    que.append((a,b))
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #print(nx, ny)
            if nx < 0 or nx >= n or ny <0 or ny >= n:
                #print("탈출")
                continue
            if graph[nx][ny]:
                graph[nx][ny]=0
                que.append((nx,ny))
                cnt+=1

    return cnt




for i in range(n):
    for j in range(n):
        if graph[i][j]:
            ans.append(bfs(graph, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)