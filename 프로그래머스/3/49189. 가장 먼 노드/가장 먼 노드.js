function solution(N, edge) {
    const graph = Array.from({length:N+1}).fill(0).map((_)=>[])
    const distance = Array.from({length:N+1}).fill(Infinity)
    distance[1]=0
    let max_distance = -Infinity
    const que = [1]
    for(let [a,b] of edge){
        graph[a].push(b)   
        graph[b].push(a)
    }
    // console.log(graph)
    while(que.length>0){
        const node = que.shift()
        for(let next_ of graph[node]){
            const dist = distance[node]+1
            // console.log(graph[node],next_,dist,distance[next_])
            if(distance[next_]>dist){
                distance[next_] = dist
                max_distance =Math.max(max_distance, dist)
                que.push(next_)
            }
            
        }
    }
    // console.log(distance, max_distance)
    const answer = []
    for(let i=0;i<N+1;i++){
        if(distance[i] == max_distance){
            answer.push(i)
        }
    }
    return answer.length;
}