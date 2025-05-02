const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = [];
rl.on('line', line => input.push(line)).on('close', () => {
  const [N, K] = input[0].split(' ').map(Number);
  const items = input.slice(1).map(line => line.split(' ').map(Number));

  // dp[i] : 무게 i까지 넣었을 때 최대 가치
  const dp = Array(K + 1).fill(0);

  for (let i = 0; i < N; i++) {
    const [w, v] = items[i];
    // 역순으로 순회해야 같은 아이템을 여러 번 사용하는 것을 방지
    for (let j = K; j >= w; j--) {
      dp[j] = Math.max(dp[j], dp[j - w] + v);
    }
  }

  console.log(dp[K]);
});
