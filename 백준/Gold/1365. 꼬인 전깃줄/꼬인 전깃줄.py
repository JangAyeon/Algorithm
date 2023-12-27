import sys
input = sys.stdin.readline

def binary_search(left, right, target):

    while left < right:
        mid = (left + right) // 2
        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right
    
N = int(input())
numbers = list(map(int, input().split()))
lis = []
lis.append(numbers[0])

for i in range(1, N):
    if lis[-1] < numbers[i]:
        lis.append(numbers[i])
    else:
        j = binary_search(0, len(lis)-1, numbers[i])
        lis[j] = numbers[i]

print(N - len(lis))