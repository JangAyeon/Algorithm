# 문제 : https://www.acmicpc.net/problem/2753

N = int(input())
if (N % 4 != 0):
    print("0")
else:  # 4의 배수임
    if (N % 100 != 0):  # 100의 배수가 아님
        print("1")
    else:  # 100의 배수
        if(N % 400 != 0):
            print("0")
        else:
            print("1")
