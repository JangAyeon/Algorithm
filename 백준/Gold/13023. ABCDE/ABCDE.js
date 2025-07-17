const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const input = [];
rl.on("line", line => input.push(line)).on("close", () => {
    const [N, M] = input[0].split(" ").map(Number);
    const arr = input.slice(1).map(item => item.split(" ").map(Number));

    const graph = Array.from({ length: N }, () => []);

    for (let [a, b] of arr) {
        graph[a].push(b);
        graph[b].push(a);
    }

    const visited = Array(N).fill(false);
    let found = false;

    function dfs(node, depth) {
        if (depth === 4) {
            console.log(1);
            process.exit(0); // 조건 만족 시 즉시 종료
        }

        for (let next of graph[node]) {
            if (!visited[next]) {
                visited[next] = true;
                dfs(next, depth + 1);
                visited[next] = false; // 백트래킹
            }
        }
    }

    for (let i = 0; i < N; i++) {
        visited[i] = true;
        dfs(i, 0);
        visited[i] = false;
    }

    console.log(0); // 아무 경우도 없을 때
});
