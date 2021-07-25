#code before lecture

n,k=map(int,input().split())
arr=[]

for _ in range(n):
    arr.append(int(input()))

left=0
right=max(arr)


while left<=right:
    mid=(left+right)//2
    cnt=0

    for x in arr:
        cnt+=x//mid
    if cnt<k:
        right=mid-1
    elif cnt>=k:
        left=mid+1

print(mid)

