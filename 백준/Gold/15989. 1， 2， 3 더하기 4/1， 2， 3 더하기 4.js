const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];

rl.on('line', function (line) {
  input.push(line);
}).on('close', function () {
  const T = parseInt(input[0]);
  const nums = input.slice(1).map(Number);
  const max = Math.max(...nums);
  
  // dp[i]: 정수 i를 1,2,3의 합으로 나타내는 방법의 수 (순서 X)
  const dp = Array(max + 1).fill(0);
  dp[0] = 1;

  const coins = [1, 2, 3];
  for (let coin of coins) {
    for (let i = coin; i <= max; i++) {
      dp[i] += dp[i - coin];
    }
  }

  for (let n of nums) {
    console.log(dp[n]);
  }
});
