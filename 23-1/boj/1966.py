import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    heap = []
    que = deque()
    n,m = map(int, input().split())
    importants = list(map(int, input().split()))
    find = importants[m]
    
    for idx, value in enumerate(importants):
        que.append([value, idx])
       
    for idx, value in enumerate(importants):
        heappush(heap,(-value))
        
    #print(heap)
    answer = 0
    flag = False
    while True and heap:
        num_= -heappop(heap)
        answer+=1
        while True and que:
            value,idx = que.popleft()
            #print(answer, que, value)
            if value < num_:
                que.append([value, idx])
                #print(que)
            elif idx ==m:
                flag = True
                print(answer)
                break
            else:
                break
        if flag:
            answer = 0
            break
        
    
    
    


    
        

