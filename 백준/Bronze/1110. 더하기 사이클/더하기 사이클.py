import sys
input = sys.stdin.readline
n = input().strip()
m=n
### 앞에서 구한 합
def get_sum(s):
    return str(int(s[0])+int(s[1]))

if int(n)<10:
    n="0"+n

answer=0

while True:
    n=n[-1]+get_sum(n)[-1]
    ##print(n)
    answer+=1
    if int(n)==int(m):
        break



print(answer)