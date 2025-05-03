const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = [];
rl.on('line', line => input.push(line)).on('close', () => {
  let T = +input[0];
  let line = 1;

  while (T--) {
    const K = +input[line++];
    const files = input[line++].split(' ').map(Number);

    // 누적합 계산
    const prefix = Array(K + 1).fill(0);
    for (let i = 0; i < K; i++) {
      prefix[i + 1] = prefix[i] + files[i];
    }

    // DP 테이블 초기화
    const dp = Array.from({ length: K }, () => Array(K).fill(0));

    // 길이 2 이상인 부분 배열만 고려
    for (let len = 2; len <= K; len++) {
      for (let i = 0; i <= K - len; i++) {
        const j = i + len - 1;
        dp[i][j] = Infinity;

        for (let k = i; k < j; k++) {
          const cost = dp[i][k] + dp[k + 1][j] + prefix[j + 1] - prefix[i];
          dp[i][j] = Math.min( cost, dp[i][j]);
        }
      }
    }

    console.log(dp[0][K - 1]);
  }
});
