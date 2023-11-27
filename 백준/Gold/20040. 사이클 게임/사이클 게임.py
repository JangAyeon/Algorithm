import sys
input = sys.stdin.readline

# 점의 갯수 N, 진행된 차례 M
N, M = map(int, input().split())
# 0 ~ n-1 고유 번호가 부여됨
parent = list(range(N))


def findParent(node, parent):
    if parent[node]!=node:
        parent[node] = findParent(parent[node], parent)
    return parent[node]
    
def findUnion(a,b, parent):
    a = findParent( a,parent)
    b = findParent( b, parent)

    # 더 작은 쪽으로 맞추기
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

flag= False
for t in range(1,M+1):
    a,b = map(int, input().split())
    # 싸이클 발생한 경우
    if findParent(a, parent) == findParent(b, parent):
        flag = True
        print(t)
        exit()
    # 싸이클 발생하지 않아 조상 할당
    findUnion(a,b, parent)

if not flag:
    print(0)
    