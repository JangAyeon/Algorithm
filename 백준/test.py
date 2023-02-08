import sys
input=sys.stdin.readline

"""
n,k=map(int, input().split())
arr = reversed([int(input().strip()) for _ in range(n)])
#print(n,k, arr)
res = 0

for i in arr:
    if i<=k:
        #print(i,k)
        #print(k//i, k%i)
        res+=k//i
        k=k%i
print(res)
"""
"""
n=int(input().strip())
arr = sorted([list(map(int, input().split())) for _ in range(n)])
arr.sort(key=lambda x:(x[1],x[0]))
#print(n, arr)
prev_end=0
res=[]

for start,end in arr:
    if prev_end<=start:
        prev_end=end
        res.append([start,end])
        #print(e,end)

print(len(res))
"""
"""
n = int(input())
city = list(map(int, input().split()))
weight = list(map(int, input().split()))
#print(n, city, weight)
min= weight[0]
res=0

for i in range(n-1):
    #print(weight[i], city[i],min)
    if min>=weight[i]:
        min=weight[i]
    res+=city[i]*min
print(res)
"""

"""
n,m=map(int, input().split())
arr = sorted(list(map(int, input().split())), key=lambda x:x//10)
arr = sorted(arr, key=lambda x :x%10)
#print(n,m,arr)
res=0

for i in arr:
    rest = i%10
    count = i//10
    if not(rest): #나머지가 없는 경우
        if m>=(count-1):
            res+=count
            m-=(count-1)
        else:
            res+=m
            m-=m
    else: #나머지가 있는 경우
        if m>=(count):
            res+=count
            m-=(count)
        else:
            res+=m
            m-=m

print(res)
"""


n,c =map(int, input().split())
m= int(input())
arr = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x : x[1])
city = [c]*(n+1)
ans = 0

for start, end, weight in arr:
    _min=c
    for i in range(start, end):
        _min=min(_min, city[i])
    _min=min(_min, weight)
    for i in range(start, end):
        city[i]-=_min
    #print(_min)
    ans+=_min
print(ans)