const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const lines = [];

rl.on("line", (line) => {
    lines.push(line.trim());
}).on("close", () => {
    const start = 1;
    const N = Number(lines[0]); // 첫 번째 입력: 노드 개수
    const graph = Array.from({ length: N + 1 }, () => []);
    const visited = Array(N + 1).fill(-1);
    const children = Array.from({ length: N + 1 }, () => new Set());

    // 간선 정보 입력
    for (let i = 1; i < N; i++) {
        const [a, b] = lines[i].split(" ").map(Number);
        graph[a].push(b);
        graph[b].push(a);
    }

    const testCase = lines[N].split(" ").map(Number); // 테스트 케이스 입력

    // BFS
    const queue = [];
    queue.push(start);
    visited[start] = 0;

    while (queue.length > 0) {
        const x = queue.shift(); // 큐에서 노드 꺼내기
        for (const i of graph[x]) {
            if (visited[i] === -1) {
                visited[i] = visited[x] + 1; // 방문 처리
                children[x].add(i); // x의 자식은 i
                queue.push(i);
            }
        }
    }

    let nextIndex = 1;
    for (const i of testCase) {
        if (nextIndex === N) break;

        const cLength = children[i].size; // 자식의 길이
        const c1 = new Set(testCase.slice(nextIndex, nextIndex + cLength));
        const c2 = children[i];

        // 자식 집합 비교
        if (!areSetsEqual(c1, c2)) {
            console.log(0);
            process.exit();
        }

        nextIndex += cLength;
    }

    console.log(1);

    // Helper function to check if two sets are equal
    function areSetsEqual(set1, set2) {
        if (set1.size !== set2.size) return false;
        for (const value of set1) {
            if (!set2.has(value)) return false;
        }
        return true;
    }
});


/**
5
1 2
2 5
1 3
3 4
1 2 3 4 5
ans: 0 
**/

/**
7
1 2
1 3
2 4
2 5
3 6
3 7
1 3 2 4 5 6 7
ans: 0 

**/