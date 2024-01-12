
    

def solution(n, wires):
    ## 각 관계를 끊고 하위 갯수 몇개인지 판별 해보기
    graph = [[] for _ in range(n+1)]
    answer = float("inf")
    
    def dfs(node, parent):
        count =1
        for child in graph[node]:
            if child !=parent:
                count +=dfs(child, node)

        return count
    
    ## 그래프 관계 입력 받기
    for wire in wires:
        a,b = wire
        graph[a].append(b)
        graph[b].append(a)
        
    ## 그래프 관계 한개씩 끊어보기
    for wire in wires:
        a,b = wire
        ## 끊어보기
        graph[a].remove(b)
        graph[b].remove(a)
        
        ## 하위 연결된거 갯수 세기
        count_a = dfs(a,b)
        count_b = n - count_a
        
        answer = min(answer, abs(count_a-count_b))
        
        ## 다시 연결하기
        graph[a].append(b)
        graph[b].append(a)

    return answer