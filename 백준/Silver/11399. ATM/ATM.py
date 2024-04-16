import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

sumList = [0]
for v in arr:
    sumList.append(sumList[-1]+v)
print(sum(sumList))