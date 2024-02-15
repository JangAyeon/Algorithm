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


#code from lecture

def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

k,n=map(int,input().split())
Line=[]
res=0
largest=0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest,tmp)

lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)


