import sys
input = sys.stdin.readline

n= int(input())
arr = sorted(list(map(int, input().split())))
distance = 1e9
answer = 0

for idx, loc in enumerate(arr):
    temp = 0
    for house in arr:
        temp += abs(loc-house)
        #print(loc, house, temp)
    if distance>temp:
        distance = temp
        answer = loc
print(answer)