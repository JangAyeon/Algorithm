# https://www.youtube.com/watch?v=94RC-DsGMLo

# 이진 탐색 코드: 재귀적 구현
def binary_search(arr, target, start, end):
    if start>end:
        return None
    
    mid = (start + end)//2
    
    # 찾은 경우 중간점 인덱스 반환
    if arr[mid] == target:
        return mid
    # 중간점의 값보다 찾는 값이 작은 경우 왼쪽 확인 필요
    elif arr[mid]>target: # 줄여야함
        return binary_search(arr, target, start, mid-1)
    # 중간점의 값보다 찾는 값이 큰 경우 오른쪽 확인 필요
    else: # 키워야 함
        return binary_search(arr, target,mid+1, end)

n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않음")
else: # 1-indexing 표기법으로 출력
    print(result +1)

# 이진 탐색 코드: 반복문 구현
def binary_search(arr, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            end = mid -1
        else:
            start = mid+1
    return None


n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않음")
else: # 1-indexing 표기법으로 출력
    print(result +1)