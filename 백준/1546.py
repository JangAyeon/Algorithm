# 백준 1546 : ttps://www.acmicpc.net/problem/1546
N = int(input())
arr = list(map(int, input().split()))
M = max(arr)

res = []
for i in arr:
    res.append(i/M*100)


print(sum(res)/len(res))
