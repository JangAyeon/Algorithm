import sys
input = sys.stdin.readline

def checkEnd(n,m):
    if n==0 and m==0:
        return True
    else:
        return False

def printResult(case, count):
    if count == 0:
        print("Case {}: No trees.".format(case))
    elif count == 1:
        print("Case {}: There is one tree.".format(case))
    else: 
        print("Case {}: A forest of {} trees.".format(case, count))

def getNode(n,m):
    graph = [[] for _ in range(n+1)]
    visitied = [False]*(n+1)
    count = 0
    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    return graph, visitied, count

def dfs(prev, curr):
    visited[curr]=True
    for next in graph[curr]:
        if next == prev:
            continue
        if visited[next]:
            return False
        if not dfs(curr, next): # 트리 순회 가능한 경우 
            return False 
    return True
            

case = 0
while True:
    case += 1
    n,m=map(int, input().split())
    flag = checkEnd(n,m)
    if flag:
        break
    else:
        graph, visited, count = getNode(n,m)
        for i in range(1, n+1):
            if not visited[i]:
                if dfs(0,i):
                    count+=1
        printResult(case, count)
