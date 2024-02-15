#code before lecture
N,K=map(int,input().split())
cnt=0
for x in range(1,N+1):
    if N%x==0:
        cnt+=1
        if cnt==K:
            print(x)
if cnt<K:
    print(-1)

#code from lecture
n,k=map(int,input().split())
cnt=0
for i in range(1,n+1):
    if n%i==0: # 약수 발견
        cnt+=1
    if cnt==k:
        print(i)
        break
else: 
    print(-1)
    #for else 구문 사용 : 정상적으로 for문이 break 없이 다 돈 경우 else문 실행됨

#code after lecture
N,K=map(int,input().split())
cnt=0
for x in range(1,N+1):
    if N%x==0:
        cnt+=1
        if cnt==K:
            print(x)
            break
else:
    print(-1)
