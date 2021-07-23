#code before lecture

N,M=map(int,input().split())
plus=[]

n=list(range(1,N+1))
m=list(range(1,M+1))

for x in n:
    for y in m:
        plus.append(x+y)

cnt=0
num=[]
for val in plus:
    if val not in num:
        if cnt<plus.count(val):
            cnt=plus.count(val)
            num.clear()
            num.append(val)
        elif cnt==plus.count(val):
            num.append(val)


for i in num:
    print(i,end=" ")

#code from lecture
n,m=map(int,input().split())
cnt=[0]*(n+m+1)
max=-2147000000
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1
for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]
for i in range(n+m+1):
    if cnt[i]==max:
        print(i,end=" ")    