const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const input = [];

rl.on('line', (line) => {
    input.push(line.trim());
}).on('close', () => {
    // 입력 처리
    const [N, M] = input[0].split(' ').map(Number);
    const ladder = input.slice(1, N + 1).map((e) => e.split(' ').map(Number));
    const snake = input.slice(N + 1).map((e) => e.split(' ').map(Number));

    // 방문 여부 및 이동 위치 배열 초기화
    const visited = Array(101).fill(false);
    const arr = Array(101).fill(0);

    // 🟢 사다리 등록
    for (let [x, y] of ladder) {
        arr[x] = y;
    }
    // 🔴 뱀 등록
    for (let [u, v] of snake) {
        arr[u] = v;
    }

// BFS 구현
function bfs() {
    const queue = [[1, 0]]; // 시작점 1번과 이동 횟수 0
    let front = 0;
    visited[1] = true;

    while (queue.length > front) {
        const [v, diceCount] = queue[front++];

        for (let i = 1; i <= 6; i++) {
            let next = v + i;

            if (next === 100) return diceCount + 1; // 100번 도착 시 반환
            if (next < 100) {
                if (arr[next] !== 0) { 
                    next = arr[next]; // 사다리 또는 뱀을 만나면 이동
                }
                if (!visited[next]) {
                    queue.push([next, diceCount + 1]); // BFS 탐색
                    visited[next] = true;
                }
            }
        }
    }
}

    // 최소 주사위 횟수 탐색
    console.log(bfs());

    process.exit();
});
