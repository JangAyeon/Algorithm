## 벨만 포드 알고리즘
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 갯수, 간선 갯수
n,m = map(int, input().split())
# 모든 간선 담는 리스트
# 출발지, 도착지, 비용
edges = [list(map(int, input().split())) for _ in range(m)]
# 최단 거리 테이블 모두 무한으로 초기화
dist = [INF]*(n+1)

def bf(start):
    # 시작 노드 초기화
    dist[start] = 0
    # 전체 n번의 라운드 반복
    for i in range(n):
        # 매 반복마다 모든 간선 확인
        for j in range(m):
            cur, next_node, cost = edges[j]
            # 현재 간선을 거쳐서 
            # 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur]!=INF and dist[next_node]>dist[cur]+cost:
                dist[next_node] = dist[cur]+cost
                # n번째 라운드에서 값이 갱신된다면 음수 순환 존재
                if i==n-1: 
                    return True

    return False
    
    
# 1번 노드가 시작 노드
negative_cycle = bf(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2,n+1):
        if dist[i]==INF:
            print(-1)
        else:
            print(dist[i])
