import sys
input =  sys.stdin.readline

n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
##print(n,m,arr)


start = end = gap=0
answer = float("inf")

while start!=n and end!=n:
    
    gap = arr[end]-arr[start]
    ##print(start, end, gap, answer)
    if gap>=m:
        start+=1
        answer=min(answer, gap)
    else:
        end+=1
        
print(answer)