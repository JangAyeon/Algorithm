# 이중우선순위큐 : https://school.programmers.co.kr/learn/courses/30/lessons/42628
# heapq 메서드 : https://python.flowdas.com/library/heapq.html 


import heapq

def solution(operations):
    que = []
    for i in operations:
        op, data = i.split()
        if op == "I":
            heapq.heappush(que,int(data))
        else:
            if len(que)>0:
                if int(data)==1:
                    que.pop(que.index(heapq.nlargest(1,que)[0]))
                elif int(data) == -1:
                    que.pop(que.index(heapq.nsmallest(1,que)[0])) # heapq.heappop(que) : 최소값 pop

    if len(que)>0:
        answer = [heapq.nlargest(1,que)[0], heapq.nsmallest(1,que)[0]]
    else:
        answer=[0,0]
    return answer



testcase = [["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"],["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]]

for test in testcase:
    print(solution(test))