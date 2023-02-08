"""
3 1
10 10 10
"""

N,M = map(int, input().split())
arr = sorted(list(map(int, input().split())), key=lambda x : x//10)
arr = sorted(arr, key=lambda x : x%10)
#print(N,M, arr)
res = 0

for i in arr:
    k = i%10
    j = i//10
    if not(k): # 나눠 떨어지는 경우
        if j-1 <= M:
            res+=j
            M-=(j-1)
        else:
            res+=M
            M-=M
    else: # 나눠 떨어지지 않는 경우
        if j<=M:
            res+=j
            M-=j
        else:
            res+=M
            M-=M

print(res)