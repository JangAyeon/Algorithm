const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


const input = []
rl.on("line", line => input.push(line)).on("close", () => {

    const N = +input[0]
    const nodes = input.slice(1).map(item => item.split(" ").map(Number))
    const graph = Array.from({
        length: N + 1
    }).map((_) => [])
    let visited = Array.from({
        length: N + 1
    }).map((_) => false)
    let distance = Array.from({
        length: N + 1
    }).map((_) => 0)
    const que = []
    let answer = 0
    // console.log(input, graph, nodes, visited)

    for (let i = 0; i < N; i++) {
        const [a, ...rest] = nodes[i]

        for (let j = 0; j < rest.length; j += 2) {
            if (rest[j] == -1) {
                continue
            }
            // console.log(rest[j], rest[j + 1])
            graph[a].push([rest[j], rest[j + 1]])
        }


    }
    // console.log(graph)

    function bfs(start) {
        que.push(start)
        visited[start] = true
        while (que.length > 0) {
            node = que.pop()
            for (let pair of graph[node]) {

                const [next_, d] = pair
                if (visited[next_]) continue
                visited[next_] = true
                que.push(next_)
                distance[next_] = distance[node] + d


            }

        }



    }

    let max = 1

    bfs(1)


    for (let i = 2; i <= N; i++) {
        max = distance[i] > distance[max] ? i : max

    }
    visited = Array.from({
        length: N + 1
    }).map((_) => false)
    distance = Array.from({
        length: N + 1
    }).map((_) => 0)
    bfs(max)
    distance.sort((a,b) => a-b)
    console.log(distance[N])




})