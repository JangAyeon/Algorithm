"""
[서로소 집합을 활용한 사이클 판별]
1. 각 간선을 확인하며 두 노드의 루트 노드를 확인함
    1-1. 루트 노드가 서로 다르다면 두 노드에 대해 union 연산 수행
    1-2. 루트 노드가 서로 같다면 사이클 발생한 것임
2. 그래프에 포함되어 있는 모든 간선에 대해 1번 과정을 반복함
"""


import sys
input = sys.stdin.readline

# 노드 갯수, 간선 수
v,e = map(int, input().split())
parent = [0]*(v+1) # 부모 테이블

def find_parent(parent, node):
    if parent[node]!=node:
        parent[node]=find_parent(parent, parent[node])
    return parent[node]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[a] = b
    else:
        parent[b] = a

# 부모 테이블 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i]=i

# 싸이클 발생 여부
isCycle = False

for _ in range(e):
    a,b = map(int, input().split())
    # 루트 노드가 같은 경우 싸이클 발생함
    # 싸이클 발생하면 종료
    if find_parent(parent, a)==find_parent(parent, b):
        isCycle = True
        break
    # 루트 노드가 같지 않은 경우 union 연산 진행
    else:
        union_parent(parent, a,b)

if isCycle:
    print("싸이클 존재함")
else:
    print("싸이클 존재하지 않음")

"""
3 3
1 2
1 3
2 3
ans: 싸이클 존재함
"""