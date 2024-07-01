import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
start, end = 0, 0
size, size_max = 0, 0
flag = 1

for start in range(n):
    while cnt <= k and end<n:
        if lst[end] % 2: ## 홀수임
            ## 제외 횟수 다 씀
            if cnt == k: 
                break
            ## 제외 횟수 아직 덜 씀 - 제외 횟수 증가
            cnt += 1
        size += 1 ## 길이 증가
        end += 1 ## tail 증가
    
    size_max = max(size_max, size-cnt)
        
    if lst[start] % 2:
        cnt -= 1
        
    size -= 1

print(size_max)