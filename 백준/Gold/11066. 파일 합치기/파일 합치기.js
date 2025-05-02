const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = [];
rl.on('line', line => input.push(line)).on('close', () => {
  let T = +input[0];
  let idx = 1;

  for (let t = 0; t < T; t++) {
    const K = +input[idx++];
    const files = input[idx++].split(' ').map(Number);

    const dp = Array.from({ length: K }, () => Array(K).fill(0));
    const prefixSum = Array(K).fill(0);
    prefixSum[0] = files[0];
    for (let i = 1; i < K; i++) {
      prefixSum[i] = prefixSum[i - 1] + files[i];
    }

    for (let len = 2; len <= K; len++) {
      for (let i = 0; i <= K - len; i++) {
        const j = i + len - 1;
        dp[i][j] = Infinity;

        for (let k = i; k < j; k++) {
          const cost = dp[i][k] + dp[k + 1][j] + (prefixSum[j] - (i > 0 ? prefixSum[i - 1] : 0));
          dp[i][j] = Math.min(dp[i][j], cost);
        }
      }
    }

    console.log(dp[0][K - 1]);
  }
});
