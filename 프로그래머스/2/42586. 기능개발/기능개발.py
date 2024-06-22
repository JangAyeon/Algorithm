import math
from collections import deque

def solution(progresses, speeds):
    
    n = len(progresses)
    deploys = deque()
    for idx in range(n):
        deploys.append(math.ceil((100-progresses[idx])/speeds[idx]))
    stack = []
    answer = []
    ##print(deploys)
    while deploys:
        
        work = deploys.popleft()
        ##print(stack,work)
        if stack and max_>=work:
            stack.append(work)
        else:
            answer.append(len(stack))
            stack=[work]
            max_=work

    if stack:
        answer.append(len(stack))
    return answer[1:]