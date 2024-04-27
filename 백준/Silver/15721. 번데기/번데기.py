import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
k = int(input())
total = 0
arr = []
temp=0

##  “뻔”이면 0, “데기”면 1
for i in range(1,10000+1):
    lst = [0,1,0,1]+[0]*(i+1)+[1]*(i+1)
    total+=len(lst)
    arr+=lst
    if total//2>=m:
        ##print(i, arr, total)
        break
count = 0
for idx in range(len(arr)):
    if arr[idx]==k:
        count+=1
        if count==m:
            print(idx%n)
