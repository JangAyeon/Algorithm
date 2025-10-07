function solution(arrows) {
    
    const directions=[
        [-1,0],// 0
        [-1,1],// 1
        [0,1], // 2
        [1,1], // 3
        [1,0], // 4
        [1,-1],// 5
        [0,-1], // 6
        [-1,-1] // 7
    ]
    const nodes = new Map()
    const routes = new Map()
    let [r,c] = [0,0] 
    nodes.set(`${r}_${c}`,true)
    let answer = 0
    
    for(let dir of arrows){
        const [dr, dc] = directions[dir]
        // console.log(dir)
        
        for(let i=0;i<2;i++){
            const [nr, nc] = [r+dr, c+dc]
            const currentKey = `${r}_${c}`
            const nextKey = `${nr}_${nc}`
            const currentRoute = `${currentKey}_${nextKey}`
            const reverseRoute = `${nextKey}_${currentKey}`
            const hasNode = nodes.get(nextKey)
            const hasRoute = routes.get(currentRoute)
            // console.log(hasNode, hasRoute)
            if(hasNode & !hasRoute){
                answer+=1
            }
            
            
            routes.set(currentRoute, true)
            routes.set(reverseRoute,true)
            nodes.set(nextKey, true)
            
            r = nr
            c = nc
            
        }
    }
    return answer;
}