const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const input = []
rl.on("line", line => input.push(line)).on("close", ()=>{
    // 정점의 개수 N과 간선의 개수 M
    const [N,M] = input[0].split(" ").map(Number)
    const arr = input.slice(1).map(item => item.split(" ").map(Number))
    const graph = Array.from({ length: N + 1 }, () => []);
    const visited = Array(N+1).fill(false)
    let answer = 0

    for(let pair of arr){
        const [a,b] = pair
        graph[a].push(b)
        graph[b].push(a)
    }
    // console.log(graph)
    function dfs(node, lst){
        
        for(let nextNode of graph[node]){
            if(!visited[nextNode]){
                // console.log(node, lst, nextNode)
                visited[nextNode] = true
                dfs(nextNode, [...lst, nextNode])
            }
            
        }
        
        
    }
    for(let i=1;i<N+1;i++){
        if(!visited[i]){
            answer+=1
            visited[i]=true
            dfs(i, [i])
        }
    }
    console.log(answer)


})