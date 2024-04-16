import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
answer =max(arr)-min(arr)
s,e =0,0
        
while True:
        if not(s <= e and e < len(arr)):
            break
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