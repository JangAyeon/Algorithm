# 문제 : https://www.acmicpc.net/problem/10951

while True:
    try:
        a, b = [int(x) for x in input().split()]
        print(a+b)
    except:
        break
