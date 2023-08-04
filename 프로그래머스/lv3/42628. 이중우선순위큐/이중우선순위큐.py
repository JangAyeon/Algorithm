

from heapq import heappush, nsmallest, nlargest


def solution(operations):
    heap = []
    for operation in operations:
        op, num = operation.split()
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
    if heap:
        answer = [nlargest(1,heap)[0],nsmallest(1,heap)[0]]
    else:
        answer = [0,0]
    return answer


