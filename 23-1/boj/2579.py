import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0]*n

if n<3:
    if n==1:
        print(arr[-1])
    elif n==2:
        print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0]+arr[1]
    for i in range(2,n):
        dp[i] = max(dp[i-2],dp[i-3]+arr[i-1])+arr[i]
    print(dp[-1])
"""
input
4
1
2
4
3

answer : 8 (1 + 4 + 3)
"""

"""
input
1
10
answer:10
"""

"""
input
3
1
100
2
Answer: 102
"""


"""
input
5
50
20
45
80
25
answer: 175
"""

"""
input
3
10
20
100
answer:120
"""