import sys
input = sys.stdin.readline

n = int(input())
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())),reverse = True)
answer = 0

for i in range(len(arr1)):
    answer +=(arr1[i]*arr2[i])
print(answer)