const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const input = [];
rl.on('line', (line) => {
    input.push(line)
}).on('close', () => {
    const N = Number(input[0]);
    const arr = input[1].split(' ').map(Number);
    const M = Number(input[2]);
    const queries = input.slice(3).map(line => line.split(' ').map(Number));

    // dp[i][j] = i~j (0-indexed)이 팰린드롬인지 여부
    const dp = Array.from({
        length: N
    }, () => Array(N).fill(0));

    // 길이 1
    for (let i = 0; i < N; i++) {
        dp[i][i] = 1;
    }

    // 길이 2
    for (let i = 0; i < N - 1; i++) {
        if (arr[i] === arr[i + 1]) dp[i][i + 1] = 1;
    }

    // 길이 3 이상
    for (let len = 3; len <= N; len++) {
        for (let start = 0; start <= N - len; start++) {
            const end = start + len - 1;
            if (arr[start] === arr[end] && dp[start + 1][end - 1]) {
                dp[start][end] = 1;
            }
        }
    }

    // 쿼리 응답
    const result = [];
    for (const [s, e] of queries) {
        result.push(dp[s - 1][e - 1]);
    }

    console.log(result.join('\n'));
});