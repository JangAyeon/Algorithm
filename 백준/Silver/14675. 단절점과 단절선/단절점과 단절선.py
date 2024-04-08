import sys
input = sys.stdin.readline

N = int(input()) #트리 정점 갯수
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def isSplitNode(k):
    if len(graph[k])>=2:
        return "yes"
    else:
        return "no"
def isSplitVertex(k):
    return "yes"

q = int(input()) # 질의 갯수
for _ in range(q):
    t,k = map(int, input().split())
    # t==1: 단절점 여부
    if t==1:
        answer = isSplitNode(k)
    # t==2: 단절선 여부
    elif t==2:
        answer = isSplitVertex(k)
    print(answer)

    