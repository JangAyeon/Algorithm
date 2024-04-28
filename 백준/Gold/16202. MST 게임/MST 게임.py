import sys
input = sys.stdin.readline

## 그래프 정점의 개수 N, 그래프 간선의 개수 M, 턴의 수 K
n,m,k = map(int, input().split())

## 두 정점의 번호 x, y
## 간선의 가중치는 주어지는 순서대로 1, 2, ..., M
graph =[]
for c in range(1, m+1):
    a,b = map(int, input().split())
    graph.append([c,a,b])

graph.sort()


def find_parent(x, parent):
    if x!=parent[x]:
        x= find_parent(parent[x],parent)
    return parent[x]

def union(a,b,parent):
    a = find_parent(a,parent)
    b = find_parent(b,parent)

    if a<b:
        parent[a]=b
    else:
        parent[b]=a

lst = graph[:]
answer = []
while k>0:
    total=0
    parent = [i for i in range(n+1)]
    flag = False
    count=0
    i =-1
    for idx, [c,a,b] in enumerate(lst):
        if find_parent(a,parent)!=find_parent(b,parent):
            union(a,b,parent)
            total+=c
            count+=1
            if not(flag):
                i=idx
                flag=True



    
    if total==0 or count!=n-1:
        break
    else:
        del lst[i]
        k-=1
        answer.append(total)
        ##print(total,count, i)

for _ in range(k):
    answer.append(0)

print(*answer)