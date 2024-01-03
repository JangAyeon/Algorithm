import sys
input = sys.stdin.readline

## 우선 순위 큐 이용해 정렬 상태 유지
from heapq import heappush, heappop

arr = []
heap = []
n = int(input())

for i in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

arr.sort() # 시작 시간 기준 정렬
heappush(heap, arr[0][1]) # 첫 회의 종료 시간을 우선순위 큐

for i in range(1,n):
    if (arr[i][0]<heap[0]): 
        # 그 다음에 있는 회의가 이전 회의보다 일찍 시작하면 새로운 회의실 사용
        heappush(heap, arr[i][1])
    else:
        # 그 다음에 있는 회의가 이전 회의 종료보다 늦게 시작하면 기존 회의실 사용
        heappop(heap)
        heappush(heap,arr[i][1])


print(len(heap))