import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0]+list(input().split())
## print(arr)
##  u학교와 v학교가 연결되어 있으며 이 거리는 d임
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2])
parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x]!=x:
        parent[x]=find_parent(parent[x])
    return parent[x]


def union(a,b):
    a = find_parent(a)
    b = find_parent(b)

    if a<b:
        parent[a]=b
    else:
        parent[b]=a
count = 0
result=0
for a,b,c in edges:
    if find_parent(a)!=find_parent(b) and arr[a]!=arr[b]:
        union(a,b)
        result+=c
        count+=1

if count==n-1:
    print(result)
else:
    print(-1)