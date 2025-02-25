import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
answer=0

for idx, v in enumerate(arr,1):
    temp = v-(idx-1)
    if temp>0:
        answer+=temp
print(answer)