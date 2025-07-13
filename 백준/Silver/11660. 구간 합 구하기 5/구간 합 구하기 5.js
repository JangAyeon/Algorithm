const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", (line) => input.push(line)).on("close", () => {
  const [N, M] = input[0].split(" ").map(Number);

  // 1. 입력받은 원본 표
  const original = input.slice(1, 1 + N).map((row) => row.split(" ").map(Number));

  // 2. 2차원 누적합 배열 (0행, 0열 padding 포함)
  const prefixSum = Array.from({ length: N + 1 }, () => Array(N + 1).fill(0));

  // 3. 누적합 배열 채우기
  for (let i = 1; i <= N; i++) {
    for (let j = 1; j <= N; j++) {
      prefixSum[i][j] =
        prefixSum[i - 1][j] +
        prefixSum[i][j - 1] -
        prefixSum[i - 1][j - 1] +
        original[i - 1][j - 1]; // 주의: original은 0-indexed
    }
  }

  // 4. 쿼리 처리
  const queries = input.slice(1 + N).map((line) => line.split(" ").map(Number));

  const results = [];
  for (const [x1, y1, x2, y2] of queries) {
    const sum =
      prefixSum[x2][y2] -
      prefixSum[x1 - 1][y2] -
      prefixSum[x2][y1 - 1] +
      prefixSum[x1 - 1][y1 - 1];
    results.push(sum);
  }

  console.log(results.join("\n"));
});
