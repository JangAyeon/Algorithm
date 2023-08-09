from heapq import heappush, nlargest, nsmallest

def solution(operations):
    heapq = []
    for operation in operations:
        op, num = operation.split()
        #print(op, num, heapq)
        if op =="I":
            heappush(heapq, int(num))
        if op == "D" and heapq:
            if int(num)==-1: # 최소값 삭제
                heapq.remove(nsmallest(1,heapq)[0])
            elif int(num)==1: # 최대값 삭제
                heapq.remove(nlargest(1,heapq)[0])
                
    if heapq:
        answer = [nlargest(1,heapq)[0], nsmallest(1,heapq)[0]]
    else:
        answer = [0,0]
    return answer