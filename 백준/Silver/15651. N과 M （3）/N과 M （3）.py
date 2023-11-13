n,m = map(int, input().split())
arr = [i for i in range(1, n+1)]

def dfs(result):
    if len(result) ==m:
        print(*result)
        return
    for num in arr:
        # 선택하는 경우
        dfs(result+[num])


for i in range(n):
    dfs([arr[i]])
    
    