import sys
input = sys.stdin.readline

def dfs(prev,node):
    visited[node]=True
    for i in graph[node]:
        if i == prev:
            continue
        if visited[i]:
            return False
        if not dfs(node, i):
            return False
        
    return True
    
case = 0
while True:
    case += 1
    N, M = map(int, input().split())
    if N == 0 and M == 0: 
        break
    graph = [[] for _ in range(N+1)] 
    #print(graph)
    visited = [False] * (N+1) # 방문 여부
    for _ in range(M):
        a, b = map(int, input().split())
        #print("a, b ",a,b, graph)
        graph[a].append(b) 
        graph[b].append(a)
    count = 0
    for i in range(1, N+1):
        if not visited[i]:
            if dfs(0, i):
                count+=1
    if count == 0:
        print("Case {}: No trees.".format(case))
    elif count == 1:
        print("Case {}: There is one tree.".format(case))
    else:
        print("Case {}: A forest of {} trees.".format(case, count))