# 문제 : https://www.acmicpc.net/problem/9498


N = int(input())

if 90 <= N <= 100:
    print("A")
elif N >= 80:
    print("B")
elif N >= 70:
    print("C")

elif N >= 60:
    print("D")
else:
    print("F")
