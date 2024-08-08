function solution(arrows) {
    // 두칸씩 이동
    // 방문한 노드
    // 방문 루트 : a->b, b->a
    let answer = 0;
    const nodes = new Map()
    const routes = new Map()
    let [r,c] = [0,0]
    nodes.set(`${r}_${c}`, true)
    const directions = [
        [-1,0], [-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]
    ]
    
    for(const d of arrows){
        const [dr, dc] = directions[d]
        for (let i=0;i<2;i++){
            let [nr, nc] = [r+dr,c+dc]
        let hasEdges = routes.has(`${r}_${c}_${nr}_${nc}`)
        let hasNode = nodes.has(`${nr}_${nc}`)
        if(hasNode && !hasEdges){
            answer+=1
        }
            nodes.set(`${nr}_${nc}`, true)
            routes.set(`${r}_${c}_${nr}_${nc}`, true)
            routes.set(`${nr}_${nc}_${r}_${c}`, true)
            r=nr
            c=nc
        }
      
    }
   
    return answer;
}