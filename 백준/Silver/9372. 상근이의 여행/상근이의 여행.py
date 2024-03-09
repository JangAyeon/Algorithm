import sys
input = sys.stdin.readline

def dfs(node, count):
    visited[node]=True

    for next_ in graph[node]:
        if not(visited[next_]):
            count = dfs(next_, count+1)
    return count


T = int(input())


for _ in range(T):
    n,m = map(int, input().split())
    
    graph = [[] for i in range(n+1)]
    visited = [False for i in range(n+1)]
    
    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(dfs(1,0))





