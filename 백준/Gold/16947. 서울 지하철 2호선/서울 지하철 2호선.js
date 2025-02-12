function createGraph(n, edges) {

    const graph = Array.from({
        length: n + 1
    }, () => []);




    // 그래프 생성
    for (const [a, b] of edges) {
        graph[a].push(b);
        graph[b].push(a);
    }
    return graph

}


function bfs(n, graph, cycle) {
    // BFS로 사이클에서 각 노드까지의 거리 계산
    const queue = [];
    for (let i = 1; i <= n; i++) {
        if (cycle[i] === 0) {
            queue.push([i, 0]);
        }
    }

    while (queue.length > 0) {
        const [current, distance] = queue.shift();
        for (const neighbor of graph[current]) {
            if (cycle[neighbor] === Infinity) { // 방문하지 않은 경우 거리 기록
                cycle[neighbor] = distance + 1;
                queue.push([neighbor, distance + 1]);
            }
        }
    }

    return cycle.slice(1); // 1번 노드부터 출력
}

function findCycle(n, edges) {

    const graph = createGraph(n, edges)
    const visited = Array(n + 1).fill(0);
    let found = false;
    const cycle = Array(n + 1).fill(Infinity); // 사이클까지 각 노드의 도달 거리
    // 사이클 탐색 (DFS)
    function dfs(path, depth) {
        if (found) return;

        const currentNode = path[path.length - 1];
        for (const neighbor of graph[currentNode]) {
            if (neighbor === path[0] && depth >= 2) { // 사이클 발견
                for (const node of path) {
                    cycle[node] = 0; // 사이클에 속하는 노드
                }
                found = true;
                return;
            }
            if (!visited[neighbor]) {
                visited[neighbor] = 1;
                dfs([...path, neighbor], depth + 1);
                visited[neighbor] = 0;
            }
        }
    }

    // 모든 노드에 대해 사이클 찾기 시도
    for (let i = 1; i <= n; i++) {
        visited[i] = 1;
        dfs([i], 0);
        visited[i] = 0;
    }
    const distance = bfs(n, graph, cycle)
    return distance


}

// 테스트 데이터
// const n = 6;
// const edges = [
//     [1, 2],
//     [3, 4],
//     [4, 6],
//     [2, 3],
//     [1, 3],
//     [3, 5]
// ];

const readline = require("readline")
const rl = readline.createInterface({

    input: process.stdin,
    output: process.stdout

})

const lines = []

rl.on("line", (line) => {
    lines.push(line.trim(0))
}).on("close", () => {
    const n = Number(lines[0])
    const edges = lines.slice(1).map((r) => r.split(" ").map(Number))
    const answer = findCycle(n, edges).join(" ")
    console.log(answer);

    //console.log("close", n, edges)
})