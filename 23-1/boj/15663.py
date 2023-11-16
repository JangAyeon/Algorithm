import sys
input = sys.stdin.readline
M, N = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False]*(M+1)
ans = []

def dfs(n,result):
    global ans
    if n==N: # 종료 조건
        ans.append(result)
        return
    prev = 0
    for i in range(M):
        if not(visited[i]) and prev!=arr[i]:
            prev = arr[i]
            visited[i]=True
            dfs(n+1, result+[arr[i]])
            visited[i]=False

dfs(0,[])
ans.sort()
for i in ans:
    print(*i)
        
        
        