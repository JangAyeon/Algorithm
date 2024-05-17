

import sys
input = sys.stdin.readline
n= max(2,int(input()))
m = int(input())

arr= []
if n>= 2:
    for num in range(n, m+1):
        flag = True
        
        for k in range(2, (num)//2+1):
            ##print(num, num%k,k)
            if num%k==0:
                flag = False
                break
        if flag:
            arr.append(num)

if len(arr):
    print(sum(arr))
    print(min(arr))
else:
    print(-1)