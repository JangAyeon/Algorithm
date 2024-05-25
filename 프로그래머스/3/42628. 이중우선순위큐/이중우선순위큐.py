from heapq import heappush, heappop
def solution(operations):
    
    answer = []
    maxHeap, minHeap = [],[]


    for op in operations:

        cmd, num = op.split()

    
        if cmd =="I":
            heappush(minHeap, int(num)) ## 뽑으면 최소값 나옴
            heappush(maxHeap, -int(num)) ## 뽑으면 최대값 (원래 숫자 부호 반대 상태) 나옴


        elif minHeap and maxHeap and cmd =="D":

            if int(num)==1: ## 최대값 삭제
                x = -heappop(maxHeap)
                minHeap.remove(x)
            else:
                x = -heappop(minHeap)
                maxHeap.remove(x)


    if maxHeap and minHeap:
        answer = [-maxHeap[0], minHeap[0]]
    else:
        answer =  [0,0]
 
    


                    

            
    return answer
