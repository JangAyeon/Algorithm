"""
[서로소 집합 계산 알고리즘]
1. union 연산을 확인하며, 서로 연결된 두 노드 A, B 확인
    1) A와 B의 루트 노드 A', B' 각각 찾기
    2) A'를 B'의 부모 노드로 설정 (주로 더 작은 노드가 부모 노드가 되도록 구현함)
2. 모든 union 연산을 처리할 때까지 1번 과정을 반복함 

"""



import sys
input = sys.stdin.readline

# 노드 갯수, 간선 갯수
v,e = map(int, input().split())
# 부모 테이블
parent = [0]*(v+1)


def find_parent(parent,node):
    if parent[node]!=node:
        parent[node]=find_parent(parent, parent[node])
    return parent[node]


def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a]=b

# 부모 테이블 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent, a,b)


## 각 원소가 속한 집합
print("각 원소가 속한 집합: ", end="")
for i in range(1, v+1):
    print(find_parent(parent,i), end=" ")
print()
## 부모 테이블 내용 출력
print("부모 테이블: ", end="")
for i in range(1, v+1):
    print(parent[i], end=" ")


"""
6 4
1 4
2 3
2 4
5 6
ans:
각 원소가 속한 집합: 1 1 1 1 5 5
부모 테이블: 1 1 1 1 5 5
"""