## 유니온 파인드로 한번 풀어보자


def find_parent(x, parent):
    if x!=parent[x]:
        x = find_parent(parent[x], parent)
    return parent[x]

def union(a,b,parent):
    a=find_parent(a, parent)
    b= find_parent(b, parent)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def solution(n, computers):
    answer = 0
    parent = [i for i in range(n)]
    
    
    for a in range(n):
        for b in range(n):
            if a==b: continue
            if computers[a][b]:
                union(a,b,parent)
    ans = set()
    for i in range(n):
        ans.add(find_parent(i,parent))
    return len(ans)