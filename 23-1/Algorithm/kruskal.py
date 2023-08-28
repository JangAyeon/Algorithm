"""
[신장트리]
하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

[크루스칼 알고리즘]
1. 간선 데이터를 비용에 따라 오름 차순 정렬
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
    2-1. 사이클이 발생하지 않는 경우, 최소 신장 트리에 포함
    2-2. 사이클이 발생하는 경우, 최소 신장 트리에 포함하지 않음
3. 모든 간선에 대해 2번 과정을 반복
"""

# 노드 갯수, 간선 갯수
v,e = map(int, input().split())
# 최종 비용 변수
result = 0

# 부모 테이블 초기화
parent = [0]*(v+1)
# 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i
    
# 모든 간선 담을 리스트
edges = []
# 모든 간선에 대한 정보 
for _ in range(e):
    a,b, cost = map(int, input().split())
    # 비용순 정렬 - 튜플 첫번째 원소를 비용 
    edges.append((cost, a,b))
edges.sort()

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x]!=x: # 루트 노드 찾을 때까지 재귀 
        parent[x]=find_parent(parent, parent[x])
    return parent[x]
    
# 두 원소가 속한 집합 합치기
def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


# 간선을 한개씩 돌면서
for edge in edges:
    cost, a,b =edge
    # 싸이클이 발생하지 않은 경우 집합에 포함함
    if find_parent(parent, a)!=find_parent(parent, b):
        union_parent(parent, a,b)
        result +=cost
        
        
print(result)

"""
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

answer: 159
"""

