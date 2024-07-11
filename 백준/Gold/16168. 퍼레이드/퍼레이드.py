import sys




#메인 코드 부분
v,e=map(int,sys.stdin.readline().split())

parents=[i for i in range(v+1)]

graph=[[] for _ in range(v+1)]

def find_parent(x):
    if x!=parents[x]:
        parents[x]=find_parent(parents[x])
    return parents[x]






def unionParent(x,y):
    x=find_parent(x)
    y=find_parent(y)

    if x<y:
        parents[y]=x
    else:
        parents[x]=y

def all_union():
    base = parents[1]
    for i in range(2, v+1):
        if parents[i]!=base:
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
        unionParent(v1,v2)

flag=False
base=find_parent(1) # 기준: 1번째 노드의 부모로 설정.
for i in range(2, v+1):
    if base!=find_parent(i):
        print('NO')
        flag=True
        break
if not(flag):
    odd_cnt=0 # 차수가 홀수인 노드 개수 카운트.
    for i in range(1,v+1):
        if len(graph[i])%2==1:
            odd_cnt+=1


    if odd_cnt==2 or odd_cnt==0:
        print('YES')
    else:
        print('NO')
