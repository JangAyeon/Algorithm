const readline = require("readline")
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})


const lines = []


rl.on("line", (line)=>lines.push(line)).on("close", ()=>{
    const [N,M] = lines[0].split(" ").map(Number)
    const arr = lines.slice(1).map(item => item.split("").map(Number))
    const visited = []
    for(let i=0;i<N;i++){
        const row = []
        for(let j=0;j<M;j++){
            row.push([0,0])
        }
        visited.push(row)
    }
    const que = [[0,0,0]] // (r,c, broken)
    visited[0][0][0]=1
    let answer = -1
    let head = 0
    // 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳
    // console.log(N,M,arr)
    // console.log(visited)
    const directions = [
        [1,0],[-1,0],[0,1],[0,-1]
    ]
    while(que.length>head){
        // console.log(head, que)
        const [r,c,broken] = que[head++]
        if(r===N-1 && c==M-1){
            answer = (visited[r][c][broken])
            break
        }
        for(let [dr, dc] of directions){
            const [nr, nc] = [r+dr, c+dc]
            if(0>nr || nr>=N || 0>nc || nc>=M){continue}
            // 벽이 아님
            if(arr[nr][nc]===0 &&visited[nr][nc][broken] ==0 ){
                visited[nr][nc][broken] = visited[r][c][broken]+1
                que.push([nr, nc, broken])
            } // 벽임 && 아직 벽 뿌신 적 없음
            else if(arr[nr][nc]===1 && broken<1 &&visited[nr][nc][broken] ==0 ){
                 visited[nr][nc][1] = visited[r][c][broken]+1
                que.push([nr, nc, broken+1])
            }
            
        }
        
    }
    console.log(answer)

})
/*
4
HELLO
DRINK
SHUTTLE
ZOO
*/