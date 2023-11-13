n = int(input())
m = int(input())
arr = list(map(int, input().split()))

height = max(arr[0]-0, n-arr[-1])


for i in range(1, len(arr)):
    temp = (arr[i]-arr[i-1]+1)//2
    height = max(temp, height)
print(height)
    