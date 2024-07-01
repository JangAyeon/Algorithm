import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
## print(n,m,arr)
answer = 0
arr.sort()

def binary(left, right, diff):
    while left<=right:
        mid = (left+right)//2
        if arr[mid]==diff:
            return True
        if arr[mid]>diff:
            right=mid-1
        else:
            left=mid+1

def check(n,m):
    if m in arr:
        return True
    else:
        left,right = 0,n-1
        while left<right:
            total = arr[left]+arr[right]
            if total>m:
                right-=1
            elif total==m:
                return True
            else:
                diff = m-total
                if arr[left]!=diff and arr[right]!=diff and binary(left, right,diff):
                    return True
                left+=1

    return False
if (check(n,m)):
    print(1)
else:
    print(0)