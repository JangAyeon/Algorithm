import sys
input = sys.stdin.readline
import math

l,w,h = map(int, input().split())
n = int(input())
cubes = [list(map(int, input().split())) for _ in range(n)]
cubes.sort(reverse=True)
total_v=total_c=answer=0
answer = 0
flag = False
for [i,count] in cubes:
    side = 2**i
    total_c *=8
    curr_count = (l//side)* (w//side)* (h//side) - total_c
    curr_count = min(curr_count, count)
    total_c+=curr_count
    answer+=curr_count
    total_v+=(side**3)*curr_count

if total_v==l*w*h:
    print(answer)
else:
    print(-1)