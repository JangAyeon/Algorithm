import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr=list(map(int, input().split()))

start = end = count = 0
total = arr[start]
while end<=n:
    ##print(start, end, total)
    if total<=m:
        if total==m:
            count+=1
        if end+1<n:
            end+=1
            total+=arr[end]
        else:
            break
    else:
        total-=arr[start]
        start+=1
        
print(count)