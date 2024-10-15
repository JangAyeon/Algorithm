import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))


start = end = total = 0
length = float("inf")


while True:
    if m<=total: ## 좀 빼야 함
        total-=arr[start]
        start+=1
        length = min(length, end-start+1)
    else:
        if n==end:
            break
        total+=arr[end]
        end+=1

        
if length==float("inf"):
    length = 0
print(length)
    
    