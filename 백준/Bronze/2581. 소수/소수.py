import sys
input = sys.stdin.readline
from collections import defaultdict


n= int(input())
m=int(input())
visited = [0 for _ in range(m+1)]


for num in range(2,int(m**(1/2))+1):
    for i in range(num*2, m+1, num):
        if not(visited[i]):
            visited[i]=1

result = 0
start = max(2,n)
index = m
for i in range(start,len(visited)):
    if not(visited[i]):
        index = min(index,i)
        result+=(i)


if result==0:
    print(-1)
else:
    print(result)
    print(index)
