#code from lecture
n,m=map(int,input().split())
a=list(map(int,input().split()))

a.sort()
left=0
right=len(a)-1

while left<=right:
    mid=(left+right)//2
    if a[mid]==m:
        print(mid+1) #0번부터 시작하는 index여서 +1
    elif a[mid]>m:
        right=mid-1
    else:
        left=mid+1