# 문제 : https://www.acmicpc.net/problem/2577

A = int(input())
B = int(input())
C = int(input())

T = A*B*C
hist = [0]*10
while T != 0:
    hist[T % 10] += 1
    T //= 10
for i in hist:
    print(i)
