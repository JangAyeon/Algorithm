#code before lecture

N=int(input())
res=[]

def money(arr):
    diff_num=len(arr)-len(set(arr))
    if diff_num==0:
        return  max(arr)*100
    elif diff_num==1:
        if arr[0]==arr[1] or arr[0]==arr[2]:
            return 1000+arr[0]*100
        else:
            return 1000+arr[1]*100
    else:
        return  10000+arr[0]*1000


for _ in range(N):
    arr=list(map(int,input().split()))
    res.append(money(arr))

print(max(res))