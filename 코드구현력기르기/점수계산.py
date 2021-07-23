import sys
sys.stdin=open("in5.txt","rt")

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
