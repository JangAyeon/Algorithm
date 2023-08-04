import sys
input = sys.stdin.readline

from heapq import heappush, heappop

T = int(input())

for _ in range(T):
    n = int(input())
    visited = [False]*1000001
    min_heap,max_heap = [],[]
    for idx in range(n):
        op, num = input().strip().split()
        if op == "I":
            heappush(min_heap, (int(num),idx))
            heappush(max_heap, (-int(num),idx))
            visited[idx] = True
        elif op == "D":
            if int(num) == -1: # 최소값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heappop(min_heap)
            elif int(num) == 1: # 최대값 삭제
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heappop(max_heap)
        
    # 이중 큐 비우기
    while min_heap and not visited[min_heap[0][1]]:
        heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heappop(max_heap)
                
    if max_heap and min_heap:
        print(-max_heap[0][0],min_heap[0][0])
    else:
        print("EMPTY")
