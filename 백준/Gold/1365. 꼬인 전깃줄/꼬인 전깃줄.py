import sys
input  = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
ans = [arr[0]] # 증가하는 부분 수열 리스트

def binarySearch(l,r,target):
    while l<r:
        mid = (l+r)//2
        if ans[mid]<target:
            l = mid+1
        else:
            r = mid
    return r

for i in range(1,n):
    if ans[-1]< arr[i]:
        ans.append(arr[i])
    else:
        idx = binarySearch(0, len(ans)-1,arr[i])
        ans[idx] = arr[i]

print(n-len(ans))
