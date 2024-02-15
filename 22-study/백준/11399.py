# 문제 : https://www.acmicpc.net/problem/11399

import sys
input = sys.stdin.readline

n = int(input().strip())
arr = sorted(list(map(int, input().split())))
res = 0

for i in range(0,len(arr)):
    #print(arr[:i+1])
    res+=sum(arr[:i+1])


print(res)