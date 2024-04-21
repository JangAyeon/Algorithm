import sys
input  = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
answer =arr[0]
for i in arr[1:]:
    answer+=i/2

print(answer)