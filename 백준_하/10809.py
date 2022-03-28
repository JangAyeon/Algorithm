# 문제 : https://www.acmicpc.net/problem/10809

# 아스키 코드 a : 97 ~ z : 122
# print(ord("z"))


dic = {}
for i in range(ord("a"), ord("z")+1):
    dic[i] = -1

N = input().lower()
for i in N:
    if dic[ord(i)] == -1:
        dic[ord(i)] = N.index(i)

for i in dic.values():
    print(i, end=" ")
