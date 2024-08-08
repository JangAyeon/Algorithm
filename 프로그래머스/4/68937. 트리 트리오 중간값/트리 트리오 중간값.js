function solution(n, edges) {
    const tree = [...Array(n+1)].map(_=>[])
    for(const [s,e] of edges){
        tree[s].push(e)
        tree[e].push(s)
    }
    
    const bfs = (start) => {
        
        const visited = Array(n+1).fill(false)
        const que = [[start,0]]
        const distance = {
            maxLen : 0,
            nodes : []
        }
        
        while(que.length){
            const [node,dist] = que.pop()
            visited[node] = true
            if(dist > distance.maxLen){
                 distance.maxLen = dist
                 distance.nodes = [node]
            } else if (dist === distance.maxLen) {
                distance.nodes.push(node)
            }
            
            for(const next_ of tree[node]){
                if(visited[next_]) continue
                que.push([next_,dist+1])
            }
        }
        return distance
    }
    
    const {nodes} = bfs(1)
    
    const leaf = bfs(nodes[0])
    if(nodes.length>1 || leaf.nodes.length>1) return leaf.maxLen
    else return leaf.maxLen-1
    
    
    
}