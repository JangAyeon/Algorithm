#code before lecture
T=int(input())
ans=[]
for i in range(T):
    N,s,e,k=map(int, input().split())
    arr=list(map(int,input().split()))
    arr_sort=sorted(arr[s-1:e]) #sorted는 반환 O
    ans.append(arr_sort[k-1])

for index,value in enumerate(ans):
    print("#"+str(index+1)+" "+str(value))



#code from lecture
T=int(input())#케이스 갯수
for t in range(T):
    n,s,e,k=map(int, input().split())
    a=list(map(int,input().split()))   
    a=a[s-1:e] 
    a.sort() #sort()는 반환 X, a 그자체를 정렬
    print("#%d %d"%(t+1,a[k-1])) #출력 형식 튜퓰 이용



#code after lecture
T=int(input())
for i in range(T):
    N,s,e,k=map(int, input().split())
    arr=list(map(int,input().split()))[s-1:e]
    arr.sort()
    print("#%d %d" %(i+1,arr[k-1]))


