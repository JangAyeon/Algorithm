import sys
input  = sys.stdin.readline

def union(a,b):
    a, b = find(a), find(b)
    if a<b:
        a,b = b,a
    parent[a] = b

def find(node):
    if node!=parent[node]:
        parent[node] = find(parent[node])
    return parent[node]

def rob():
    for i in range(1, n+1):
        if i==parent[i]:
            for j in range(k-1, cntFriends[i]-1, -1):
                dp[j] = max(dp[j], dp[j-cntFriends[i]]+candy[i])
            

n,m,k = map(int, input().split())
candy = [0] + list(map(int, input().split()))
parent = [i for i in range(n+1)]
cntFriends = [1]*(n+1)

for i in range(m):
    a,b = map(int, input().split())
    union(a,b)

for node in range(1,n+1):
    if node!=parent[node]:
        root = find(node)
        candy[root]+=candy[node]
        cntFriends[root]+=cntFriends[node]

dp = [0 for _ in range(k)]
rob()
print(max(dp))
        