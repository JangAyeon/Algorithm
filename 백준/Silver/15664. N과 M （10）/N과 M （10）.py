n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []

def dfs(idx, result):
    global visited
    if len(result) ==m:
        print(*result)
        return
    prev =-1
    for i in range(idx, n):
        # 선택하는 경우
        if not(visited[i]) and prev!=arr[i]:
            visited[i]=True
            dfs(i+1,result+[arr[i]])
            visited[i]=False
            prev=arr[i]

            

     

prev = -1
for i in range(n):
    visited=[False]*(n)
    visited[i]=True
    if prev!=arr[i]:
        dfs(i+1,[arr[i]])
        prev = arr[i]

    
