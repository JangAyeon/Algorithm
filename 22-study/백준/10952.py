#문제 : https://www.acmicpc.net/problem/10952


while True:
    a,b=[int(x) for x in input().split()]
    if ((a==0)&(b==0)):
        break
    else:
        print(a+b)