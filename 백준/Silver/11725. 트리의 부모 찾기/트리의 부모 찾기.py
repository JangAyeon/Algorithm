import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

n = int(input())
parent = [0]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a, b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(node):
    for child in graph[node]:
        if parent[child]==0:
            parent[child] = node
            dfs(child)
    
dfs(1)    
print(*parent[2:], sep="\n")