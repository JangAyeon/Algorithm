import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def countPoint(root):
    count[root]=1
    for i in tree[root]:
        if not count[i]:
            countPoint(i)
            count[root]+=count[i]



n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
count = [0]*(n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

countPoint(r)

for i in range(q):
    u = int(input())
    print(count[u])