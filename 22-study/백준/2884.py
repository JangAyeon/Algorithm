# 문제 : https://www.acmicpc.net/problem/2884

H, M = map(int, input().split())
#print(H, M)
if (M-45) < 0:
    MM = 60+(M-45)
    if (H-1) < 0:
        HH = 24+(H-1)
    else:
        HH = H-1
else:
    MM = M-45
    HH = H

print(HH, MM)
