import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
buttons=[]

if m != 0:
    buttons += list(map(int, input().split()))


minimum = abs(100 - n)

for i in range(999999):
    num = str(i)

    for j in num:
        if int(j) in buttons:
            break

    else:
        minimum = min(minimum, abs(n - i) + len(num))

print(minimum)