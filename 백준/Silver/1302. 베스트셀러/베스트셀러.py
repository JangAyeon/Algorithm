import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
arr = list(input().strip() for _ in range(n))
max_count=0
max_title=[]
counter = Counter(arr)
for key,value in counter.items():
    ##print(key, value)
    if value>max_count:
        max_count=value
        max_title=[key]
    elif value==max_count:
        max_title.append(key)

max_title.sort()
print(max_title[0])