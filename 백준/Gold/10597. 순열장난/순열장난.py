import sys
input = sys.stdin.readline



arr = input().strip()

if len(arr)<10:
    N = len(arr)
else: 
    N =9+(len(arr)-9)//2




def dfs(idx, lst):
    if idx == len(arr):
        print(*lst)
        exit()

    # 1자리수 check
    num1 = int(arr[idx])
    if not visited[num1]:
        visited[num1] = 1
        dfs(idx + 1, lst+[num1])
        visited[num1] = 0

    # 2자리수 check
    if idx+1 < len(arr):
        num2 = int(arr[idx:idx+2])
        if num2 <= N and not visited[num2]:
            visited[num2] = 1
            dfs(idx+2, lst+[num2])
            visited[num2] = 0




visited = [0 for _ in range(N + 1)]

dfs(0, [])

"""
155987643211011121314
"""