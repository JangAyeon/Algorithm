import sys
input = sys.stdin.readline


def findParent(node, parent):
    if parent[node]!=node:
        parent[node] = findParent(parent[node],parent)
    return parent[node]

def findUnion(a,b, parent):
    a = findParent(a, parent)
    b = findParent(b, parent)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 건물 갯수 N, 도로 갯수 M
N,M = map(int, input().split())
edges = []
parent = [i for i in range(N+1)]


for _ in range(M):
    a,b, cost = map(int, input().split())
    edges.append((cost, a,b))

edges.sort()

total = 0
result=0
for edge in edges:
    cost, a,b = edge
    total+=cost
    if findParent(a,parent)!=findParent(b, parent):
        findUnion(a,b,parent)
        result+=cost

cnt = 0
for i in range(1, N+1):
    if parent[i]==i:
        cnt+=1

if cnt>1:
    print(-1)
else:
    print(total-result)