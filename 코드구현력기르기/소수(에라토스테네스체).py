#code before/after lecture
N=int(input())
cnt=[0]*(N+1)
ans=[]
for i in range(2,N+1): #소수는 0,1은 미포함임으로 2부터 시작
    if cnt[i]==0:
        ans.append(i) #ans에 소수 추가하고
        for j in range(i,N+1,i):
            cnt[j]+=1
            
print(len(ans)) #len으로 소수 갯수 출력

#code from lecture
n=int(input())
ch=[0]*(N+1)
cnt=0 #갯수 세는 변수
for i in range(2,n+1): #2~n까지 iter 돌아야함
    if ch[i]==0:
        cnt+=1
        for j in range(i,n+1,i): #간격 i로 i의 배수로
            ch[j]=1
print(cnt)