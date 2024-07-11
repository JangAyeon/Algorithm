import sys




#메인 코드 부분
v,e=map(int,sys.stdin.readline().split())

parents=[i for i in range(v+1)]

graph=[[] for _ in range(v+1)]

def find_parent(x):
    if x!=parents[x]:
        parents[x]=find_parent(parents[x])
    return parents[x]






def union(x,y):
    x=find_parent(x)
    y=find_parent(y)

    if x<y:
        parents[y]=x
    else:
        parents[x]=y




def all_union():
    base = find_parent(1)
    for i in range(2, v+1):
        if find_parent(i)!=base:
            return False
    return True


def able_degree():
    odd_count =0
    for i in range(1,v+1):
        if len(graph[i])%2==1:
            odd_count+=1
    if odd_count==0 or odd_count==2:
        return True
    
    else:
        return False


for _ in range(e):
    v1,v2=map(int,sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
    if parents[v1]!=parents[v2]:
        union(v1,v2)




if all_union():
    if able_degree():
        print("YES")
    else:
        print("NO")
else:
    print("NO")