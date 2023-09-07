// day11: 통증2

const readline = require("readline");
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
let n;
let a;
let b;

rl.on("line", (line) => {
  input.push(line);
  if (input.length === 2) {
    rl.close();
  }
});

function game(dp, n) {
  for (let i = a; i <= n; i++) {
    if (i - b >= 0 && dp[i][1] > dp[i - b][1] + 1) {
      dp[i] = [i - b, dp[i - b][1] + 1];
    }
    if (i - a >= 0 && dp[i][1] > dp[i - a][1] + 1) {
      dp[i] = [i - a, dp[i - a][1] + 1];
    }

    //console.log(i, dp[i])
  }
}

function getAnswer(dp) {
  if (dp[n][1] === Infinity) {
    return -1;
  } else {
    return dp[n][1];
  }
}

rl.on("close", () => {
  n = Number(input[0]);
  [a, b] = input[1].split(" ").map(Number);
  const dp = new Array(n + 1).fill([0, Infinity]);
  // 이전 값 계산 횟수
  //dp[1] = [1,0];
  dp[a] = [0, 1];
  dp[b] = [0, 1];
  //console.log(dp)
  game(dp, n);
  //console.log(dp);
  //console.log(n,a,b);
  const answer = getAnswer(dp);
  console.log(answer);
  process.exit();
});
