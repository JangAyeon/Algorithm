from collections import defaultdict

def solution(arrows):
    directions=[[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
    r=c=0
    answer = 0
    nodes = defaultdict(bool)
    edges =  defaultdict(bool)
    nodes[f"{r}_{c}"]=True
    
    for dir in arrows:
        for _ in range(2):
            nr, nc = r+directions[dir][0],  c+directions[dir][1]
            if(( nodes[f"{nr}_{nc}"] and not( edges[f"{r}_{c}_{nr}_{nc}"]))):
                answer+=1
            
            nodes[f"{nr}_{nc}"]=True
            edges[f"{r}_{c}_{nr}_{nc}"]=True
            edges[f"{nr}_{nc}_{r}_{c}"]=True
            r, c=nr, nc
            

    return answer