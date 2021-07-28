#code before lecture

n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
cnt=0
tmp=[True]*n

for i in range(len(arr)):

    if (tmp[i]):
        tmp[i]=False
        cnt+=1

        for j in range(i+1,len(arr)):
            if (tmp[j]):
                if arr[i]+arr[j]<=m:
                        tmp[j]=False
                        break


print(cnt)

#code from lecture
n,limit=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
cnt=0
while p:
    if len(p)==1: 
        #한 명만 남은 경우는 그냥 limit 따지지 않고 탈출
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop() #가장 무거운 사람 탈출
        cnt+=1
    else:
        p.pop(0)
        p.pop()
        cnt+=1
print(cnt)