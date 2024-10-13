import sys
input = sys.stdin.readline


def isPalindrome(arr):
    start, end = [0, len(arr)-1]
    checked = 0
    while(start<end):
        if arr[start]==arr[end]:
            start+=1
            end-=1
        else:
            ##print(start, end)
            if start<=end-1: ## 오른쪽 제거
                rm = arr[:end]+arr[end+1:]
                reverse_rm = list(reversed(rm))
                ##print(rm, reverse_rm)
                if rm==reverse_rm:
                    return 1
            if start+1<=end: ## 왼쪽 제거
                rm = arr[:start]+arr[start+1:]
                reverse_rm = list(reversed(rm))
                ##print(rm, reverse_rm)
                if rm==reverse_rm:
                    return 1
                
            return 2
        
    return 0
    

n = int(input())
for _ in range(n):
    arr = list(input().strip())
    print(isPalindrome(arr))