# 문제 : https://www.acmicpc.net/problem/2675

N = int(input())
arr = [input().split() for i in range(N)]

# print(arr)
for i in arr:
    for j in list(str(i[-1])):
        print(j*int(i[0]), end="")
    print()
