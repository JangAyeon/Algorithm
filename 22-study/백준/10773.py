# 문제 : https://www.acmicpc.net/problem/10773


N = int(input())
arr = []

for i in range(N):
    M = int(input())
    if M == 0:
        arr.pop()
    else:
        arr.append(M)

print(sum(arr))
