const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const input = [];
rl.on('line', line => input.push(line)).on('close', () => {
   // 수 갯수 N, 합 구하는 횟수 M
  	const [N,M] = input[0].split(" ").map(Number)
    const dp = [new Array(N+1).fill(0),...input.slice(1,N+1).map(item => [0,...item.split(" ").map(Number)])]
    const T = input.slice(N+1).map(item => item.split(" ").map(Number))
    // console.log(dp)
    for(let i=1;i<=N;i++){
        for(let j=1; j<=N;j++){
            const num = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+dp[i][j]
            dp[i][j]=num
        }
    }
    for(let[x1,y1,x2,y2] of T){
        const answer = dp[x2][y2]-(dp[x1-1][y2]+dp[x2][y1-1]-dp[x1-1][y1-1])
        console.log(answer)
    }
    // console.log(N,M, T)
    
});