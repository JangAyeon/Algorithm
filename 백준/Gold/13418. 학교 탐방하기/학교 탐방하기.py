import sys
input = sys.stdin.readline


def find(node):
    if parent[node]!=node:
        parent[node] = find(parent[node])
    return parent[node]

def union(a,b):
    a,b = find(a), find(b)

    if rank[a]>=rank[b]:
        parent[b] = a
        if rank[a]==rank[b]:
            rank[a]+=1
    else:
        parent[a]=b

N,M = map(int, input().split())

# 부모 저장
parent=[i for i in range(N+1)]
# 각 노드마다 랭크 저장
rank = [0]*(N+1)
edges=[]
for i in range(M+1):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))

# 비용 기준 정렬
edges.sort()

ascend=0 
for i in range(M+1):
    cost, a, b = edges[i]
    if find(a)!=find(b):
        union(a,b)
        ascend+=cost

# 부모 저장
parent=[i for i in range(N+1)]
# 각 노드마다 랭크 저장
rank = [0]*(N+1)
decend = 0

for i in range(M,-1,-1):
    cost, a,b =edges[i]
    if find(a)!=find(b):
        union(a,b)
        decend+=cost

print((N-ascend)**2 - (N-decend)**2)
    