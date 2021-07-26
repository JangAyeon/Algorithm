#code with lecture

n,c=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
lt=arr[0]
rt=arr[-1]
res=0

def Count(mid):
    cnt=1
    start=arr[0]
    for i in range(len(arr)):
        dis=abs(start-arr[i])
        if dis>=mid:
            start=arr[i]
            cnt+=1

    return cnt



while (lt<=rt):
    mid=(lt+rt)//2
    print("mid: ",mid,"cnt: ",Count(mid))
    
    #모든 말의 거리가 mid보다 작거나 같음
    if (Count(mid)>=c): 
        #주어진 말보다 더 많은 갯수의 말을 배치 할 수 있는 경우에 주어진 말의 갯수는 당연히 배치 가능
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)


#code from lecture

def Count(len):
    cnt=1
    ep=Line[0]
    for i in range(1,n):
        if Line[i]-ep>=len: #말 배치 가능
            cnt+=1
            ep=Line[i]


n,c=map(int,input().split())
Line=[]
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()

lt=1 #최소거리 1
rt=Line[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)
