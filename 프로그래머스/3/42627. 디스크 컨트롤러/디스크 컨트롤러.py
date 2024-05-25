import heapq

def solution(jobs):
    answer = 0
    now = 0 #현재시간
    i = 0   #처리개수
    start = -1 #마지막 완료시간
    heap = []
    
    while i < len(jobs):
        for job in jobs: ## 주어진 작업 중에 현재 시점에서 처리 가능한 작업
            if start < job[0] <= now: 
                heapq.heappush(heap,[job[1],job[0]])
        
        if heap: ## 처리 가능한 작업들 싹 다 처리 
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += now - current[1] #요청으로부터 처리시간
            i += 1 ## 처리 완료한 작업 갯수 +1
            
        else: ## 처리할 수 있는 작업 없는 경우 시간 증가
            now += 1
            
    return answer // len(jobs)