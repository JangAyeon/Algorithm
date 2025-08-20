const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => lines.push(line)).on("close", () => {
  const [m, n] = lines[0].split(" ").map(Number);

  const LIMIT = 10000001; // 10^7 + 1
  const a = new Array(LIMIT).fill(0);

  // 초기화
  for (let i = 2; i < LIMIT; i++) {
    a[i] = i;
  }

  // 에라토스테네스의 체
  for (let i = 2; i <= Math.sqrt(LIMIT); i++) {
    if (a[i] === 0) continue;
    for (let j = i + i; j < LIMIT; j += i) {
      a[j] = 0;
    }
  }

  let cnt = 0;
  for (let i = 2; i < LIMIT; i++) {
    if (a[i] !== 0) {
      let tmp = BigInt(i) * BigInt(i);
      while (tmp <= BigInt(n)) {
        if (tmp >= BigInt(m)) {
          cnt++;
        }
        tmp *= BigInt(i);
      }
    }
  }

  console.log(cnt);
});
