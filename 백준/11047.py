import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(reversed([int(input().strip()) for _ in range(n)]))
#print(n,m,arr)
res = 0

for i in arr:
    if m>=i:
        res +=(m//i)
        m = m%i
    #print(i, res)

print(res)
