# https://www.acmicpc.net/problem/15661

import sys
input = sys.stdin.readline
from itertools import combinations

n= int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]
idx = [x for x in range(n)]
ans = 2147000000
#print(n, arr, idx, ans)


def get_diff(start, link):
    stats_start = 0
    stats_link = 0
    
    for i, j in combinations(start, 2):
        stats_start += arr[i][j] + arr[j][i]
    for i, j in combinations(link, 2):
        stats_link += arr[i][j] + arr[j][i]
    return abs(stats_start - stats_link)


for i in range(1, n//2+1):
    #print(i)
    start=tuple(combinations(idx, i))
    link = tuple(combinations(idx, n-i))
    size=len(start)
    #print(start, link)
    for j in range(size):
        diff=get_diff(start[j], link[size-1-j])
        ans=min(ans, diff)

print(ans)