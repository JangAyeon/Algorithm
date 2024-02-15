#code before lecture : fail
 
n,m=map(int,input().split())
arr=list(map(int,input().split()))

size=n//m
first_mid=size
second_mid=first_mid+size

left=0
right=sum(arr)

total=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(k+1,len(arr)):
            total_1=arr[:i]
            total_2=arr[i:j]
            total_3=arr[j:]

#code from lecture
def Count(capacity):
    #해당 용량으로 N곡을 다 저장하려면 dvd 몇장이 필요한가
    cnt=1
    sum=0
    for x in Music:
        if sum+x>capacity: #이 곡이 추가되었을 때 용량 초과된 경우
            cnt+=1 #dvd 용량 초과되어서 새로운 dvd 한장 필요
            sum=x #새로운 dvd에 x 추가
        else:
            sum+=x
    return cnt


n,m=map(int,input().split())
Music=list(map(int,input().split()))
maxx=max(Music)

lt=1
rt=sum(Music)
res=0
while(lt<rt):
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        #dvd 용량이 가장 큰 노래 한곡보다는 커야함 
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)
