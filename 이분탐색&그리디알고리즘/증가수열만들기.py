#code before lecture : fail
n=int(input())
arr=list(map(int,input().split()))

start=0
end=len(arr)-1
ans=[-2147000000]
res=""

while start<=end:
    print("ans: ",ans,"start: ",start,"end: ",end)

    if (arr[start]<arr[end]):
        if (arr[start]>=ans[-1]):
            ans.append(arr[start])
            res+="L"
            start+=1
        elif (arr[end]>=ans[-1]):
            ans.append(arr[end])
            res+="R"
            end-=1
    elif  (arr[start]>arr[end]):
        if (arr[end]>=ans[-1]):
            ans.append(arr[end])
            res+="R"
            end-=1
        elif (arr[start]>=ans[-1]):
            ans.append(arr[start])
            res+="L"
            start+=1
    else:
        if (arr[end]>=ans[-1]):
            ans.append(arr[end])
            end-=1
        break
            
print(len(ans[1:]))
print(res)

#code from lecture
n=int(input())
a=list(map(int,input().split()))
lt=0
rt=n-1
last=0
res=""
tmp=[]
while lt<=rt:
    if a[lt]>last:
        tmp.append(a[lt],"L")
    if a[rt]>last:
        tmp.append(a[rt],"R")
    #lt값과 rt값 모두 last보다 큰 경우 더 작은 값 넣어야 함
    tmp.sort()
    if len(tmp)==0:
        #더이상 가져올 것이 없는 경우
        break
    else:
        res+=tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=="L":
            lt+=1
        else:
            rt-=1

    tmp.clear()
print(len(res))
print(res)

