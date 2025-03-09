const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []
const directions = [
    [0,-1],[0,1],
    [1,0],[-1,0]
]

function bfs(r,c, isSick, visited, graph,N){
    const que = [[r,c]]
    const color = graph[r][c]
    visited[r][c]=true
    while (que.length>0){
        const [r,c] =  que.shift()
        for (let [dr, dc] of directions){
            const [nr, nc] = [r+dr, c+dc]
            // 범위 나감, 방문함
            if (!(0<=nr && nr<N) || !(0<=nc && nc<N) || (visited[nr][nc])){
                continue
            }
            if (isSick && ((color =="B" && graph[nr][nc]=="B") || (color!="B" && graph[nr][nc]!="B"))){
                visited[nr][nc] = true
                que.push([nr, nc])                
            }
            else if (!isSick && (graph[nr][nc] ===color)){
                visited[nr][nc] = true
                que.push([nr, nc])
            }
        }
    }
}
    

rl.on("line", (line) => {

    lines.push(line.trim())

}).on("close", () => {

    const N = Number(lines[0])
    const graph = lines.slice(1).map(e => e.split(""))
    // console.log(N, graph)
    const answer = [0,0]


    for (let idx = 0; idx<answer.length;idx++){
        const isSick = idx==0?false: true
        const visited = Array.from(Array(N), ()=> Array(N).fill(false))
        for(let i=0;i<N;i++){
            for(let j=0; j<N;j++){
                if(!visited[i][j]){
                    answer[idx]+=1
                    bfs(i, j, isSick, visited, graph,N)
                }
                
            }
        }
    }
    console.log(answer.join(" "))
})