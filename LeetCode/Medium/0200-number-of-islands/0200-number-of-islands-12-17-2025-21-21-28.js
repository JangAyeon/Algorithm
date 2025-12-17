/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {

    const [N,M] = [grid.length, grid[0].length]
    const visited = Array.from({length:N}).fill(0).map(()=> Array.from({length:M}).fill(false))
    // console.log(visited)
    let answer = 0
    const directions = [
        [-1,0],[1,0],[0,-1],[0,1]
    ]

    function bfs(rr,cc){
        const que = [[rr,cc]]
        visited[rr][cc]=true
        while(que.length){
            const [r,c] = que.shift()
            for(let [dr,dc] of directions){
                const [nr, nc] = [r+dr,c+dc]
                if(nr<0 || nc< 0 || nr>=N || nc>=M || visited[nr][nc] || grid[nr][nc]!="1"){continue}
                visited[nr][nc] = true
                que.push([nr, nc])
            }
        }
    }

    for(let r=0;r<N;r++){
        for(let c = 0; c<M;c++){
            if(!visited[r][c] && grid[r][c]=="1"){
                answer++
                bfs(r,c)
            }
        }
    }

    // console.log(answer)
    return answer
    
};