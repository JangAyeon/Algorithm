const readline = require("readline")
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

const lines = []
rl.on("line", line => lines.push([...line])).on("close", ()=>{
    // console.log(lines)
    function isSafe(r, c, t) {
      // t초 후 벽이 내려온 위치 확인
      const nr = r - t;
      return nr <0|| lines[nr][c] !== "#"; // nr<0이면 이미 사라진 벽
}

    const [N,M] = [lines.length, lines[0].length]
    const directions=[
        [0,0], // 현재 위치
        [0,1], [0,-1] , [1,0],[-1,0], [1,1],[-1,-1], [-1,1],[1,-1]
    ]

    function bfs(){
            const visited = Array.from({ length: N }, () =>
        Array.from({ length: N }, () => Array(directions.length).fill(false))
      );
    visited[N-1][0][0] = true
    const que = [[N-1, 0,0]] // (r,c, time)
    while(que.length){
        const [r,c,t] = que.shift()
        if(r==0&&c==N-1)return 1
        for(let [dr,dc] of directions){
            const [nr, nc, nt] =[r+dr, c+dc,  Math.min(t + 1, 8)]
            // const 범위나감 = nr<0 || nr>=N || nc<0 || nc>=M
            if(nr<0 || nr>=N || nc<0 || nc>=M) continue
             // 이동 직후 벽이 없어야 하고, 벽이 내려온 후에도 안전해야 함
              if (!isSafe(nr, nc, t) || !isSafe(nr, nc, t + 1)) continue;
      if (!visited[nr][nc][nt]) {
        visited[nr][nc][nt] = true;
        que.push([nr, nc, nt]);
      }
        }
    }
return 0
    }

console.log(bfs())



})