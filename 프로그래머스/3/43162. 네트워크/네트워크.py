## 유니온 파인드로 한번 풀어보자
## https://school.programmers.co.kr/questions/55001

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
    parent = [i for i in range(n+1)]
    
    
    for a in range(1, n+1):
        for b in range(1, n+1):
            if computers[a-1][b-1]:
                if (find_parent(a,parent)==find_parent(b,parent)):
                    continue
                
                union(a,b,parent)
    ans = set()
    print(parent)
    for x in range(1, n+1):
        ans.add(find_parent(x, parent))
    print(parent)
    return len(ans)