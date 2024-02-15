import sys
n = int(input())
arr = sorted(list(map(int,input().split())))
m = int(input())
search = list(map(int,input().split()))


for num in search:
    start, end = 0, len(arr)-1
    flag  = False
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == num:
            print(1)
            flag = True
            break
        elif arr[mid]>num: # 줄여야 함
            end = mid-1
        else:
            start = mid+1
    if not(flag):
        print(0)
