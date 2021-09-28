#code before lecture
#import sys
#sys.stdin=open("in5.txt","r")


c,n=map(int,input().split())
arr=[]
res=[]
for i in range(n):
    arr.append(int(input()))

def DFS(L,w):
    if w>c:
        return
    else:
        if L==n:
            res.append(w)
            return
        else:
            res.append(w)
            DFS(L+1,w+arr[L])
            DFS(L+1,w)

DFS(0,0)
print(max(res))

#code from lect

def DFS(L,sum,tsum):
    global result 
    #메인에서 선언한 result 사용 
    # 이거 없으면 이 함수 내에서 따로 result라는 지역 변수 사용
    if sum+(total-tsum)<result:
        return
    if sum>c: #무게 제한 넘음
        return 
    if L==n: #부분 집합 하나 완성됨
        if sum<result:
            result+=sum
    else:
        DFS(L+1,sum+a[L],tsum+a[L])
        DFS(L+1,sum,tsum+a[L])


c,n=map(int,input().split())
a=[0]*n 
result=-2147000000
for i in range(n): #입력이 줄바꿈으로 들어옴
    a[i]=int(input())
total=sum(a)
DFS(0,0,0)
print(result)