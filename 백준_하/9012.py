# 문제 : https://www.acmicpc.net/problem/9012


N = int(input())
arr = [input() for _ in range(N)]


for i in arr:
    stack = 0
    # print("### : ", i)
    for j in i:
        if j == "(":
            stack += 1
        else:
            stack -= 1
        if stack == -1:
            break
    if stack == 0:
        print("YES")
    else:
        print("NO")
