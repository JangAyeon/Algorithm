import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline



def dfs(x):
    global result
    visited[x]=True
    cycle.append(x)
    pair=arr[x]

    if visited[pair]:
        if pair in cycle:
            result+=cycle[cycle.index(pair):]
        return
    else:
        dfs(pair)
            
    
T = int(input())

for _ in range(T):
    n = int(input())
    arr = [0]+list(map(int, input().split()))
    visited = [False]*(n+1)
    result = []
    for idx in range(1, len(arr)):
        if not(visited[idx]):
            cycle = []
            dfs(idx)
    print(n-len(result))