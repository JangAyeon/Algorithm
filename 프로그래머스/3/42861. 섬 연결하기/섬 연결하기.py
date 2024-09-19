### 유니온 파인드로 풀어보자
def find_parent(x, parent):
    if x!=parent[x]:
        x = find_parent(parent[x],parent)
    return parent[x]

def union(a,b,parent):
    a=find_parent(a,parent)
    b=find_parent(b,parent)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:(x[2]))
    parent=[i for i in range(n)]
    for a,b,c in costs:
        if find_parent(a, parent)!=find_parent(b,parent):
            union(a,b,parent)
            answer+=c
            
    return answer