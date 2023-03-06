



def solution(info, edges):
    visited = [False] * len(info)
    answer = []


    def dfs(sheep, wolf):
        if sheep>wolf:
            answer.append(sheep)
        else:
            return
        
        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child]=True
                if info[child] == 0: # sheep인 경우
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[child]=False
    # 루트 노드에서 시작
    visited[0]=True
    dfs(1, 0) # 루트 노드는 언제나 항상 양
    return max(answer)


testcase = [[[0,0,1,1,1,0,1,0,1,0,1,1],	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]]	, [[0,1,0,1,1,0,1,0,0,1,0],	[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]]]
for info, edges in testcase:
    print(solution(info,edges))