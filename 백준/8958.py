# 문제 : https://www.acmicpc.net/problem/8958

from importlib.abc import ResourceLoader


N = int(input())
arr = [input() for _ in range(N)]
res = []


for i in arr:
    ans = [0]
    for j in range(len(i)):
        #print("i[j]", i[j])
        if i[j] == "O":
            if j == 0:
                ans.append(1)
            else:
                if (i[j-1] == i[j]):
                    ans.append(ans[-1]+1)
                else:
                    ans.append(1)
    res.append(sum(ans))

for i in res:
    print(i)
