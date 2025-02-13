const readline = require("readline")
const rl = readline.createInterface({

    input: process.stdin,
    output: process.stdout
})


const lines = []


rl.on("line", (line) => {

    lines.push(line.trim())
}).on("close", () => {
    const [N, M] = lines[0].split(" ").map(Number)
    const graph = lines.slice(1).map((r) => r.split(""))
    const visited = new Array(N).fill(0).map((_) => new Array(M).fill(false))

    const directions = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]
    let hasCycle = false

    function dfs(r, c, type, path) {
        //console.log(r,c, type)
        if (hasCycle) {
            return
        }
        const curr = path[path.length - 1]
        for (let dir of directions) {

            const [dr, dc] = dir
            const [nr, nc] = [r + dr, c + dc]
            // 범위 밖
            if (!(0 <= nr && nr < N && 0 <= nc & nc < M)) {
                continue
            }
            const next_ = graph[nr][nc]
            const last_loc = `${nr}_${nc}`
            const first_loc = path[0].join("_")
            //console.log(first_loc , last_loc, first_loc == last_loc)
            // 같은 색 & 길이 3부터 & 가장 첫번째 노드와 위치 동일함
            if (next_ == type && last_loc === first_loc && path.length >= 3) {
                hasCycle = true
                return
            }
            // 같은 타입 아님 | 이미 방문함
            if (next_ == type && !visited[nr][nc]) {

                visited[nr][nc] = true
                dfs(nr, nc, type, [...path, [nr, nc]])
                visited[nr][nc] = false
            }


        }


    }

    for (let i = 0; i < N; i++) {

        for (let j = 0; j < M; j++) {
            visited[i][j] = true
            //console.log("start",i,j)
            dfs(i, j, graph[i][j], [
                [i, j]
            ])
            visited[i][j] = false
        }
    }

    const answer = hasCycle ? "Yes" : "No"
    console.log(answer)

})