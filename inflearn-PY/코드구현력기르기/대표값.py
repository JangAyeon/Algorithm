#code before lecture
N=int(input())
arr=list(map(int,input().split()))
avg=round(sum(arr)/len(arr))

res=float("inf")
score=[]

for i,x in enumerate(arr):
    if res>abs(avg-x):
        res=abs(avg-x)
        score.clear()
        score.append(x)
    elif res==abs(avg-x):
        score.append(x) 


print(avg,arr.index(max(score))+1)

#code from lecture
n=int(input())
a=list(map(int,input()))
ave=round(sum(a)/n+0.5) #평균
min=2147000000

for idx, x in enumerate(a):
    tmp=abs(x-ave) #거리값
    if tmp<min:
        min=tmp
        score=x
        res=idx+1 # 0번 index부터 시작해서 +1
    
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1

print(avg, res)


