import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,r,q = map(int, input().split())
tree = [[] for _ in range(n+1)]
count = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(root):
    count[root]=1
    for node in tree[root]:
        if not(count[node]):
            dfs(node)
            count[root]+=count[node]
            
            
dfs(r)

for i in range(q):
    u = int(input())
    print(count[u])
            
