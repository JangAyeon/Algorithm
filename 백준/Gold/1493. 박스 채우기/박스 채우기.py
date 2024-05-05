import sys
input = sys.stdin.readline

l,w,h = map(int, input().split())
total_v  = l * w * h
n = int(input())
cubes = []
for i in range(n):
    s, count = map(int, input().split())
    s = 2**s
    ## 부피, 한변, 갯수
    cubes.append([s*s*s, s, count])


curr_v = 0
answer = 0
cubes.sort(reverse=True)
for v, s, c in cubes:

    curr_v*=8
    curr_c = (l//s)*(w//s)*(h//s)-curr_v
    curr_c = min(curr_c, c)
    answer+=curr_c
    curr_v+=curr_c

if curr_v==total_v:
    print(answer)
else:
    print(-1)