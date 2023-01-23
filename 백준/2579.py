import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.insert(0,0)
ans  = [0]*(n+1)

if n==1:
    notStepped = 0
else:
    ans[1], ans[2]=arr[1], arr[2]
    if n>2:
        ans[3]= arr[3]
        for i in range(4, n+1):
            ans[i] = min(ans[i-2], ans[i-3])+arr[i]
    notStepped = min(ans[n-1],ans[n-2])
print(sum(arr)- notStepped)
