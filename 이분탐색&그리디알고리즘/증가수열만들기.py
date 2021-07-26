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
