import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def countPoint(root):
    visited[root]=1
    for i in tree[root]:
        if not visited[i]:
            countPoint(i)
            visited[root]+=visited[i]



n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

countPoint(r)

for i in range(q):
    u = int(input())
    print(visited[u])