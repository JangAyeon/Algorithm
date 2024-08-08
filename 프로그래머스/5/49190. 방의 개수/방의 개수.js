
    


function solution(arrows) {
    const directions=[
    
    [-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]
    
]
   
    const edges = new Map()
    const nodes = new Map()
    let [r,c] = [0,0]
    let answer = 0
    nodes.set(`${r}_${c}`, true)
    for(let dir of arrows){
for(let i=0;i<2;i++){
            let [nr, nc] = [r+directions[dir][0], c+directions[dir][1]]
        let hasEdges = edges.has(`${r}_${c}_${nr}_${nc}`)
        let hasNode = nodes.has(`${nr}_${nc}`)
        if(hasNode && !hasEdges){
            answer+=1
        }
        nodes.set(`${nr}_${nc}`,true)
        edges.set(`${r}_${c}_${nr}_${nc}`,true)
        edges.set(`${nr}_${nc}_${r}_${c}`,true)
        r=nr
        c=nc
}

    }
    return answer;
}