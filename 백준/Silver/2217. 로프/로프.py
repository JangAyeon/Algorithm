import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
answer = 0

arr.sort(reverse=True)
for i in range(0,n):
    w = (i+1)*arr[i]
    answer = max(answer, w)

print(answer)