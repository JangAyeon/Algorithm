# 우선 순위 큐 라이브러리 이용한 힙 정렬 구현
# min-heap으로 오름차순 정렬
# https://www.youtube.com/watch?v=AjFlp951nz0

import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    
    # 모든 원소를 차례로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례로 꺼내 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
res = heapsort(arr)

for i in range(n):
    print(res[i])