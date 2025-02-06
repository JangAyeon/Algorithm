const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []
function solve(danceSteps) {
    danceSteps.unshift(0);
    danceSteps.pop();
    
    const power = Array.from({ length: 5 }, () => Array(5).fill(0));
    
    // 같은 지점을 누를 때 1의 힘 사용
    for (let i = 0; i < 5; i++) {
        power[i][i] = 1;
    }
    
    // 중앙에서 다른 지점으로 이동할 때 2의 힘 사용
    for (let i = 1; i < 5; i++) {
        power[0][i] = power[i][0] = 2;
    }
    
    // 인접 지점 이동 시 3의 힘 사용
    const adjacentMoves = [[1, 2], [1, 4], [2, 1], [2, 3], [3, 2], [3, 4], [4, 1], [4, 3]];
    adjacentMoves.forEach(([a, b]) => {
        power[a][b] = power[b][a] = 3;
    });
    
    // 반대편으로 이동 시 4의 힘 사용
    const oppositeMoves = [[1, 3], [2, 4], [3, 1], [4, 2]];
    oppositeMoves.forEach(([a, b]) => {
        power[a][b] = power[b][a] = 4;
    });
    
    const MAX = 400001;
    const n = danceSteps.length;
    const dp = Array.from({ length: n }, () => 
        Array.from({ length: 5 }, () => Array(5).fill(MAX))
    );
    
    dp[0][0][0] = 0;
    
    for (let i = 1; i < n; i++) {
        const v = danceSteps[i];
        
        // 왼발 이동
        for (let l = 0; l < 5; l++) {
            for (let r = 0; r < 5; r++) {
                dp[i][v][r] = Math.min(dp[i][v][r], dp[i - 1][l][r] + power[l][v]);
            }
        }
        
        // 오른발 이동
        for (let l = 0; l < 5; l++) {
            for (let r = 0; r < 5; r++) {
                dp[i][l][v] = Math.min(dp[i][l][v], dp[i - 1][l][r] + power[r][v]);
            }
        }
    }
    
    let minPower = MAX;
    for (let l = 0; l < 5; l++) {
        for (let r = 0; r < 5; r++) {
            minPower = Math.min(minPower, dp[n - 1][l][r]);
        }
    }
    
    console.log(minPower);
}

rl.on("line", (line) => {
    lines.push(line.trim())
}).on("close", () => {
    const arr = lines[0].split(" ").map(Number)
solve(arr)




})