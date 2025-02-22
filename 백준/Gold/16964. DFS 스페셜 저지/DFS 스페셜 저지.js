const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const input = [];

rl.on('line', (line) => {
    input.push(line.trim());
}).on('close', () => {
    let N = input[0] * 1;
    let graph = Array.from(Array(N - 1), () => Array());
    let graph_list = Array.from(Array(N + 1), () => Array());
    let visited = new Array(N + 1).fill(false);

    for (let i = 1; i < input.length - 1; i++) {
        let values = input[i].split(' ').map(Number);
        for (let j = 0; j < values.length; j++) {
            graph[i - 1][j] = values[j];
        }
    }

    for (let [a, b] of graph) {
        graph_list[a].push(b);
        graph_list[b].push(a);
    }

    let nCheck = input[input.length - 1].split(' ').map(Number);
    let output = 0;
    let end = false;
    let pi = 1; // 값이 들어갈 인덱스

    if (nCheck[0] === 1) {
        visited[1] = true;
        DFS(1);
    }

    console.log(output);

    function DFS(n) {
        if (pi === N) {
            output = 1;
            end = true;
            return;
        } else if (!end) {
            let nArr = [];
            for (let i = 0; i < graph_list[n].length; i++) {
                if (!visited[graph_list[n][i]]) {
                    nArr[graph_list[n][i]] = true;
                }
            }
            for (let i = 0; i < graph_list[n].length; i++) {
                if (nArr[nCheck[pi]] !== undefined) {
                    pi += 1;
                    visited[nCheck[pi - 1]] = true;
                    DFS(nCheck[pi - 1]);
                } else {
                    let allVisited = true;
                    for (let j = 0; j < graph_list[n].length; j++) {
                        if (!visited[graph_list[n][j]]) {
                            allVisited = false;
                            break;
                        }
                    }
                    if (!allVisited) {
                        output = 0;
                        end = true;
                        return;
                    }
                }
            }
        }
    }
});
