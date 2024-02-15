#code before lecture

N=int(input())
arr=list(map(int,input().split()))
res=[]
for i in range(N):
    if i==0:
        if arr[i]==1:
            cnt=1
        else:
            cnt=0
    else:
        if arr[i]==1:
            cnt+=1
        else:
            cnt=0
    res.append(cnt)

print(sum(res))


#code from lecture : 리스트 사용 X
n=int(input())
a=list(map(int,input().split()))
sum=0
cnt=0
for x in a:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0
print(sum)