import sys
input = sys.stdin.readline




def find(node):
    if(parent[node]!=node):
        parent[node] = find(parent[node])
    return parent[node]

def union(a,b):
    a, b = find(a), find(b)
    parent[max(a,b)] = min(a,b)

def check(a,b):
    return find(a)==find(b)

## 통로 간 거리 구하기
def dist(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)

n,m =  map(int, input().split())
parent = [i for i in range(n)]
cord, graph = [],[]
answer = 0

for _ in range(n):
    x,y = map(int, input().split())
    cord.append((x,y))
## 이미 연결되었다고 한 곳 조상 통일해서 연결 지어주기
for _ in range(m):
    x,y=map(int, input().split())
    union(x-1, y-1)

# 거리 구해서 그래프에 넣음
for i in range(n-1):
    for j in range(i+1, n):
        graph.append((i,j, dist(cord[i], cord[j])))

graph.sort(key=lambda x:x[2]) # 정렬
for i in graph:
    if not(check(i[0], i[1])):
        union(i[0], i[1])
        answer+=i[2]


print('%.2f'%(answer))