import sys
input = sys.stdin.readline

# 노드 갯수, 간선 갯수
v, e = map(int, input().split())

# 최종 비용 변수
answer = 0

# 부모 테이블 초기화
parent = [0]*(v+1)

# 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보 
edges = []
for _ in range(e):
    start, end, cost = map(int, input().split())
    edges.append((cost, start, end))
edges.sort() # 간선 정보를 비용 기준으로 정렬


# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
        
for edge in edges:
    cost, start, end = edge
    if find_parent(parent, start) != find_parent(parent, end):
        union_parent(parent, start, end)
        answer +=cost
    
     
print(answer)
