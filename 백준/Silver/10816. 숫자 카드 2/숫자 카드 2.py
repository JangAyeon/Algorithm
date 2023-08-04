import sys
n = int(input())
arr = sorted(list(map(int,input().split())))
m = int(input())
search = list(map(int,input().split()))

def binary_search(arr, target, start, end):
    if start>end:
        return 0 # 존재하지 않음
        
    mid = (start + end)//2
    
    # 찾은 경우 갯수 반환
    if arr[mid] == target:
        return count[target]
        
    # 중간점의 값보다 찾는 값이 작은 경우 왼쪽 확인 필요
    elif arr[mid]>target: # 줄여야함
        return binary_search(arr, target, start, mid-1)
    # 중간점의 값보다 찾는 값이 큰 경우 오른쪽 확인 필요
    else: # 키워야 함
        return binary_search(arr, target,mid+1, end)

count={}
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

answer = []
#print(count)
for num in search:
    print(binary_search(arr, num, 0, len(arr)-1), end = " ")
    

        
        
