# 문제 : https://www.acmicpc.net/problem/1010
# https://lar542.github.io/Python/2019-07-11-python2/


import math


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    ans = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(ans)
