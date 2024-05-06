import sys
input = sys.stdin.readline

n = int(input())
arr =list(map(int, input().split()))

heights = [0]*(1000000+1)

count = 0
for curr_h in arr:
    if heights[curr_h]==0:
        count+=1
        heights[curr_h-1]+=1
    else:
        heights[curr_h]-=1
        heights[curr_h-1]+=1

print( sum(heights))