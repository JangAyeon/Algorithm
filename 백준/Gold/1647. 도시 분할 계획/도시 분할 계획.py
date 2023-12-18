import sys
input = sys.stdin.readline


def find(node):
    if parent[node]!=node:
        parent[node] = find(parent[node])
    return parent[node]

def union(a,b):
    a,b = find(a), find(b)
    if a==b:
        return
    if rank[a]>rank[b]:
        parent[b] = a
    elif rank[b]>rank[a]:
        parent[a] = b
    else:
        parent[a]=b
        rank[b]+=1

N,M = map(int, input().split())
graph=[]
# 부모 저장
parent=[i for i in range(N+1)]
# 각 노드마다 랭크 저장
rank = [0]*(N+1)

for i in range(M):
    a,b,cost = map(int, input().split())
    graph.append((a,b,cost))

# 비용 기준 정렬
graph.sort(key=lambda x:x[2])

answer=0 # 연결된 마을 길이
end_=0 # 마지막에 연결된 마을 길이

for i in graph:
    if find(i[0])!=find(i[1]):
        union(i[0], i[1])
        answer+=i[2]
        end_=i[2]

print(answer-end_)