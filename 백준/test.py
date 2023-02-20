import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]
idx = list(range(n))
ans = float("inf")

def getDiff(start, link):
    score={"start":0, "link":0}
    for x,y in combinations(start,2):
        score["start"]+=arr[x][y]+arr[y][x]
    for x,y in combinations(link,2):
        score["link"]+=arr[x][y]+arr[y][x]
    return abs(score["start"]-score["link"])

for i in range(1, n//2+1):
    start =  tuple(combinations(idx, i))
    link = tuple(combinations(idx, n-i))
    #print("start", start)
    #print("link", link)
    length = len(start)
    for i in range(length):
        _min=getDiff(start[i], link[length-1-i])
        if ans>_min:
            ans=_min
print(ans)