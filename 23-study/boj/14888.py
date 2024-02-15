import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
add, sub,mul, div = map(int, input().split())


def dfs(n, total, add, sub,mul,div):
    global min_, max_
    if n==N:
        min_=min(min_, total)
        max_=max(max_, total)
        return
    
    if add>0:
        dfs(n+1, total+arr[n], add-1, sub, mul, div)
    if sub>0:
        dfs(n+1, total-arr[n], add, sub-1, mul, div)
    if mul>0:
        dfs(n+1, total*arr[n], add, sub, mul-1, div)
    if div>0:
        dfs(n+1, int(total/arr[n]), add, sub, mul,div-1)
    

min_,max_ = int(1e9), -int(1e9)
dfs(1, arr[0], add, sub,mul, div)
print(max_, min_,sep = "\n")