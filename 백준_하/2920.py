# 문제 : https://www.acmicpc.net/problem/2920

N = list(map(int, input().split()))
# print(N)
if(N == sorted(N)):
    print("ascending")
elif (N == list(reversed(sorted(N)))):
    print("descending")
else:
    print("mixed")
