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

#code from lecture
L=int(input())
a=list(map(int, input().split()))
m=int(input())

a.sort()
for _ in range(m):
    a[0]+=1
    a[L-1]-=1
    a.sort()
print(a[L-1]-a[0])