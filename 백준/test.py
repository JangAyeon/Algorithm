"""
#1654
import sys
input=sys.stdin.readline

k,n= map(int, input().split())
arr=[int(input().strip()) for _ in range(k)]
start,end=1, max(arr)

while start<=end:
    mid=(start+end)//2
    ans=0
    for i in arr:
        ans+=i//mid
    if ans>=n:
        start=mid+1
    else:
        end=mid-1

print(end)


#2805
import sys
input=sys.stdin.readline

n,m= map(int, input().split())
arr=list(map(int, input().split()))
start,end= 0, max(arr)-1

while start<=end:
    mid=(start+end)//2

    total=sum([i-mid for i in arr if i>=mid])
    #print(total)

    if total>=m:
        start=mid+1
    else:
        end=mid-1
print(end)


#2295
import sys
input=sys.stdin.readline

n = int(input())
arr = set(list(int(input().strip()) for _ in range(n)))
dic = {}
ans=0

for k in arr: #{k-x,k}
    for x in arr:
        diff = k-x
        if diff>=0 and dic.setdefault(diff,k)<k:
            dic[diff]=k

for y in arr:
    for z in arr:
        add = y+z
        k=dic.get(add)
        if k and k>ans:
            ans=k

print(ans)
"""

from itertools import combinations
import sys
input=sys.stdin.readline

n,m = map(int, input().split())
chicken=[]
house=[]

for i in range(n):
    for j,idx in enumerate(input().split()):
        if idx=="1":
            house.append((i,j))
        elif idx=="2":
            chicken.append((i,j))

min_chicken = float("inf")

for x in combinations(chicken, m):
    curr_dist=0
    for i,j in house:
        min_dist=float("inf")
        for k,l in x:
            min_dist=min(min_dist, (abs(i-k)+abs(j-l)))
        curr_dist+=min_dist
        #print(min_dist, curr_dist)
    min_chicken=min(min_chicken, curr_dist)
print(min_chicken)