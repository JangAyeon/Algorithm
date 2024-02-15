# 백준 : https://www.acmicpc.net/problem/11650

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for a, b in sorted(arr):
    print(a, b)
