import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = -1

if n%2!=0:
    answer = arr.pop()
while arr:
    answer = max(arr.pop(0)+arr.pop(), answer)

print(answer)