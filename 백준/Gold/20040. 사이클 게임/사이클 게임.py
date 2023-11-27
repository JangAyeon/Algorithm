import sys
input = sys.stdin.readline

def findParent(node, parent):
    if parent[node]!=node:
        parent[node] = findParent(parent[node], parent)
    return parent[node]

def findUnion(parent, a, b):
    a = findParent(a, parent)
    b = findParent(b, parent)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

# 점의 갯수, 진행된 차례 
n,m = map(int, input().split())
parent  = [i for i in range(n)] 
flag = False

for t in range(m):
    a, b = map(int, input().split())
    if findParent(a, parent)==findParent(b, parent):
        flag = True
        print(t+1)
        break
    if flag==False:
        findUnion(parent, a,b)
    else:
        break
if flag==False:
    print(0)
    