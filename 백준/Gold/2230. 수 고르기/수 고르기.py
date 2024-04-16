import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()


s = 0
e=0
answer =max(arr)-min(arr)

while (s <= e and e < len(arr)):
        diff =  arr[e]-arr[s]
        if diff==m:
            answer = m
            break
        elif diff>m:
            answer = min(diff, answer)
            s+=1
        else:
            e+=1



print(answer)
"""
3 3
1
5
3
ans:4
"""

"""
5 3
1
2
3
4
5
ans: 3
"""

"""
5 6
1
2
3
4
11
ans: 7
"""

"""
2 2000000000
-1000000000
1000000000

"""

"""
7 4
1
8
15
16
17
18
22
"""