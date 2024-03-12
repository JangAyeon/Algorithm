import sys
input = sys.stdin.readline





def dfs(idx, ans):
    if idx==len(arr):
        if len(ans)==6:
            print(*ans)
        return

    dfs(idx+1, ans+[arr[idx]])
    dfs(idx+1, ans)





while True:
    lst = list(map(int, input().split()))
    if len(lst)>1:
        n, arr = lst[0],lst[1:]
        dfs(0,[])
        print()
    else:
        break
        
    