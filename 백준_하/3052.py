# 문제 : https://www.acmicpc.net/problem/3052

arr = [(int(input()) % 42) for _ in range(10)]
print(len(set(arr)))
