#code before lecture

n=int(input())
arr=list(map(int, input().split()))
m=int(input())

for i in range(m):
    idx_max=arr.index(max(arr))
    idx_min=arr.index(min(arr))
    arr[idx_max]-=1
    arr[idx_min]+=1

print(max(arr)-min(arr))