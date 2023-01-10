# 문제 : https://www.acmicpc.net/problem/2577
import sys

N = 3
arr = [int(sys.stdin.readline().strip()) for i in range(N)]
# print(arr)


mul = 1
for i in arr:
    mul *= i
# print(mul)

arr_cnt = list(map(int, str(mul)))
for i in range(10):
    print(arr_cnt.count(i))
