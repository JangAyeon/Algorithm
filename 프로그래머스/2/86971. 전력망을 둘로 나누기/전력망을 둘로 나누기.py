from collections import deque

def solution(n, wires):
    answer = float("inf")
    graph =[[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    for x,y in wires:
        que =  deque()
        que.append(x)
        count = 0
        visited = [False]*(n+1)
        visited[x] = True

        while que:
            x = que.popleft()
            count+=1
            for next_ in graph[x]:
                if next_ != y and not(visited[next_]):
                    visited[next_]=True
                    ##print(x,next_,count)
                    que.append(next_)

        
        #print(count, n-count, abs(n-count-count))       
        answer = min(answer, abs(n-count-count) )
            

    return answer