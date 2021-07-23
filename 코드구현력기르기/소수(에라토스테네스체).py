#code before/after lecture
N=int(input())
cnt=[0]*(N+1)
ans=[]
for i in range(2,N+1):
    if cnt[i]==0:
        ans.append(i)
        for j in range(i,N+1,i):
            cnt[j]+=1
            
print(len(ans))

#code from lecture
n=int(input())
ch=[0]*(N+1)
cnt=0 #갯수
for i in range(2,n+1): #2~n까지 iter 돌아야함
    if ch[i]==0:
        cnt+=1
        for j in range(i,n+1,i): #간격 i로 i의 배수로
            ch[j]=1
print(cnt)