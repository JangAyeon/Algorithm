import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

start = end = total = 0
answer=0

while True:
    if total>=m:
        if total==m:
            answer+=1
        total-=arr[start]
        start+=1
    
    elif end==len(arr):
        break
    else:
        total+=arr[end]
        end+=1
print(answer)
