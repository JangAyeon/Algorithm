import sys
input = sys.stdin.readline

n ,c =map(int, input().split())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]
arr.sort(key=lambda x : x[1])
res = [c]*(n+1)
ans = 0

#print(n,c,arr, res)

for s,e,w in arr:
    #print(s,e,w)
    _min = c
    for i in range(s,e):
        _min= min(_min,res[i])
    _min=min(_min,w)
    for i in range(s,e):
        res[i]-=_min
    ans+=_min
print(ans)
