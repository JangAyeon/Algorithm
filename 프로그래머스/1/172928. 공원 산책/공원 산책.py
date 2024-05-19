


def solution(park, routes):
    graph = []
    start = [-1,-1]
    ops= {"N":[-1,0],"S":[1,0],"W":[0,-1],"E":[0,1]}
    R=len(park)
    C = len(park[0])
    
    ## 그래프 한줄씩 받으면서 Start 지점 찾기
    for i,row in enumerate(park):
        row = list(row)
        graph.append(row)
        if "S" in row:
            start = [i, row.index("S")]
    r,c = start                  
    for route in routes:
        op,count = route.split()
        ##print(ops[op],int(count))
        nr, nc = r,c
        for i in range(int(count)):
            flag=True
            nr+=ops[op][0]
            nc+=ops[op][1]
            ##print(nr, nc)
            if not(0<=nr<R) or not(0<=nc<C)  or graph[nr][nc]=="X":
                flag=False
                break
        if flag:
            r,c=nr,nc

                
            
        
    ## 동서남북 방향 지표 찾기
    
    answer = [r,c]
    return answer