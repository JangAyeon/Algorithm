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