const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout

})
const input = []
rl.on("line", line => input.push(line)).on("close", () => {
    const [N, M] = input[0].split(" ").map(Number)
    const graph = input.slice(1).map((row) => row.split("").map(Number))
    // const visited = Array.from({
    //     length: N
    // }, () => Array.from({
    //     length: M
    // }, () => false))


    const dr = [1, -1, 0, 0]
    const dc = [0, 0, -1, 1]
// console.log(N, M, graph)
    function bfs(a, b) {


        const que = [
            [a, b]
        ]
        // visited[a][b] = true

        while (que.length > 0) {
            const [r, c] = que.shift()
            // console.log(r, c)
            if (r == N - 1 && c == M - 1) {
                console.log(graph[N-1][M-1])
                return
            }
            for (let idx = 0; idx < 4; idx++) {
                const [nr, nc] = [r + dr[idx], c + dc[idx]]
                // 
                // 범위 벗어난 경우
                if (nr < 0 || nr >= N || nc < 0 || nc >= M || graph[nr][nc] != 1) continue
                // console.log(nr, nc, graph[nr][nc], d)
                graph[nr][nc] = graph[r][c]+1
                que.push([nr, nc])


            }

        }

    }
    bfs(0, 0)
    
})