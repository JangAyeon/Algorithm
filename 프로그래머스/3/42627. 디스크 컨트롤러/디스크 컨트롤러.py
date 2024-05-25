from heapq import heappop, heappush

def solution(jobs):
    jobs.sort(key=lambda x:x[1])
    start=0
    n = len(jobs)
    answer = []

            
    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0]<=start:
                
                
                start+=jobs[i][1]
                answer.append(start-jobs[i][0])
                jobs.pop(i)
                break
            if i==len(jobs)-1:
                start+=1
                
                

        
    return sum(answer)//len(answer)