const readline = require("readline")
const rl = readline.createInterface({

    input: process.stdin,
    output: process.stdout
})

const lines = []
const directions = [


    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, +1],
    [+1, -1],
    [+1, 0]
]

rl.on("line", (line) => {
    const s = line.trim()
    lines.push(s)
}).on("close", () => {
    const N = Number(lines[0])
    const graph = lines.slice(1).map(r => r.split(""))
    const colors = Array.from({
        length: N
    }, () => Array(N).fill(-1));
    let answer = 0

    function dfs(r, c, type) {
        colors[r][c] = type
        answer = Math.max(answer, 1)
        for (let [dr, dc] of directions) {
            const [nr, nc] = [r + dr, c + dc]
            if (nr < 0 || nc < 0 || nr >= N || nc >= N) {
                continue
            }
            // 번갈아 가면서 두기 0 1 0 1 0 1
            if (graph[nr][nc] === "X" && colors[nr][nc] === -1) {
                dfs(nr, nc, type === 1 ? 0 : 1)
                answer = Math.max(2, answer)

            }
            // 인접 노드가 나랑 값이 같으면 하나 더 색깔 추가
            if (colors[nr][nc] === type) {
                answer = Math.max(answer, 3)
            }

        }
    }

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < N; j++) {
            if (graph[i][j] === 'X' && colors[i][j] === -1) {
                dfs(i, j, 0);
            }
        }
    }
    console.log(answer)
})

/**
3
X-X
XX-
---
ans: 2
**/