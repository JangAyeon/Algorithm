import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]
idx = list(range(n))
ans = 2147000000

def getDiff(start, link):
    s_score=0
    l_score=0
    for x,y in combinations(start,2):
        s_score+=arr[x][y]+arr[y][x]
    for x,y in combinations(link,2):
        l_score+=arr[x][y]+arr[y][x]
    return abs(s_score-l_score)

for i in range(1, n//2+1):
    start =  tuple(combinations(idx, i))
    link = tuple(combinations(idx, n-i))
    #print("start", start)
    #print("link", link)
    length = len(start)
    for i in range(length):
        ans = min(ans, getDiff(start[i], link[length-1-i]))
print(ans)