import sys
input = sys.stdin.readline

from heapq import heappush, nsmallest, nlargest

T = int(input())

for _ in range(T):
    n = int(input())
    heap = []
    for _ in range(n):
        op, num = input().strip().split()
        if op == "I":
            heappush(heap, int(num))
        elif op == "D" and heap:
            if int(num) == -1: # 최소값 삭제
                value = nsmallest(1, heap)[0]
                #print(value, heap)
                heap.remove(value)
            elif int(num) == 1: # 최대값 삭제
                value = nlargest(1, heap)[0]
                heap.remove(value)
                
                
    if len(heap) == 0:
        print("EMPTY")
    else:
        print(nlargest(1,heap)[0], " ",nsmallest(1,heap)[0])
