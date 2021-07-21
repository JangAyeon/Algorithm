
#code before lecture
from itertools import combinations

N,K=map(int,input().split())
arr=list(map(int,input().split()))
ans=[]
for i in combinations(arr,3):
    if sum(i) not in ans:
        ans.append(sum(i))

ans.sort(reverse=True)
print(ans[K-1])

#code from lecture
n,k=map(int,input().split())
a=list(map(int,input().split()))
res=set()#집합 -> 중복 제거
for i in range(n): #첫번째 수
    for j in range(i+1,n): #두번째 수 : 첫번째 수 뒷편에서 수 뽑기
        for m in range(j+1,n): #세번째 수 #두번째 수 뒷편에서 수 뽑기
            #위와 같은 3중 for문으로 수 뽑으면 중복 없음
            res.add(a[i]+a[j]+a[m]) #집합 요소 추가 : add

res=list(res) #set은 정렬 개념 X -> list 타입으로 변환
res.sort(reverse=True) #내림차순
print(res[k-1])

#code after lecture
from itertools import combinations

N,K=map(int,input().split())
arr=list(map(int,input().split()))
res=set()
for i in combinations(arr,3):
    res.add(sum(i))
res=list(res)
res.sort(reverse=True)
print(res[K-1])