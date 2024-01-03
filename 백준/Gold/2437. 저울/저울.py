import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()


target=1
for n in arr:
    if target<n:
        break

    target +=n
print(target)