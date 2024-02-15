import sys
input = sys.stdin.readline

INF = int(1e9)
n,m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
distance = [INF]*(n+1)


def isNegativeCycle(start):
    flag = False
    distance[start] = 0
    
    for i in range(n): # n번(turn)의 갱신 진행
        for start, end, cost in edges: # 매 반복마다 모든 간선 확인
            if distance[start]!=INF and distance[end]>cost+distance[start]:
                distance[end]=cost+distance[start]
                if i == n-1: # 마지막 turn까지 값이 갱신된다면 음수 순환 존재
                    flag=True
                    
    return flag
    
if isNegativeCycle(1):
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i]==INF:
            print(-1)
        else:
            print(distance[i])
