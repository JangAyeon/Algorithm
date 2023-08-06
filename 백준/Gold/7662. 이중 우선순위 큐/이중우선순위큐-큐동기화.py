import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 큐 동기화
def async_heapq(visited, heapq):
    while heapq and not(visited[heapq[0][1]]):
        heappop(heapq)
      
T = int(input())

for _ in range(T):
    q = int(input())
    min_heap = []
    max_heap = []
    visited = [False]*q
    for idx in range(q):
        cmd, num = input().strip().split() # 바로 입력 받아 계산 수행
        if cmd == "I":
            heappush(min_heap, (int(num), idx)) # 최소힙
            heappush(max_heap, (-int(num), idx)) # 최대힙
            visited[idx] = True
        elif cmd=="D":
            if int(num)==1: # 최대값 삭제
                # 최소힙 상태와 동기화
                async_heapq(visited, max_heap)
                if max_heap:
                    num, idx = heappop(max_heap)
                    visited[idx] = False
                
            elif int(num)==-1: # 최솟값 삭제
                # 최대힙 상태와 동기화
                async_heapq(visited, min_heap)
                if min_heap:
                    num, idx = heappop(min_heap)
                    visited[idx] = False
        
        # 최종 동기화
        async_heapq(visited,min_heap)
        async_heapq(visited, max_heap)
            
    if max_heap and min_heap: # 최대힙 부호 전환해야 함
        print(-heappop(max_heap)[0],heappop(min_heap)[0])
    else:
        print("EMPTY")
            
