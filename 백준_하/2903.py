# 문제 : https://www.acmicpc.net/problem/2908

N, M = input().split()
print(max(int(N[::-1]), int(M[::-1])))
