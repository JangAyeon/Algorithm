from collections import deque

n,m,k = map(int, input().split())
graph= [[0]*(n+1) for _ in range(n+1)]
bfs_visited=[False]*(n+1) 
dfs_visited=[False]*(n+1) 

for _ in range(m):
    x,y = map(int, input().split())
    graph[x][y]=graph[y][x]=1

def dfs(graph, k, visited):
    visited[k] = True
    print(k, end= " ")
    for i in range(1,n+1):
      if not visited[i] and graph[k][i]:
        dfs(graph, i, visited)


def bfs(graph, k, visited):
    visited[k]=True
    que=deque([k])

    while que:
        v = que.popleft()
        print(v,end =" ")
        for i in range(1,n+1):
            if not visited[i] and graph[v][i]:
                que.append(i)
                visited[i]=True

dfs(graph, k, dfs_visited)
print()
bfs(graph, k,bfs_visited)