const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const permutations = [
  [9, 3, 1],
  [9, 1, 3],
  [3, 9, 1],
  [3, 1, 9],
  [1, 9, 3],
  [1, 3, 9],
];

const visited = Array.from({ length: 61 }, () =>
  Array.from({ length: 61 }, () => Array(61).fill(false))
);

let input = [];

rl.on("line", (line) => {
  input.push(line.trim());
}).on("close", () => {
  const N = parseInt(input[0]);
  const hp = input[1].split(" ").map(Number);
  while (hp.length < 3) hp.push(0); // 항상 3개로 맞춰주기

  const queue = [];
  queue.push([...hp, 0]); // [a, b, c, count]
  visited[hp[0]][hp[1]][hp[2]] = true;

  while (queue.length > 0) {
    const [a, b, c, cnt] = queue.shift();

    if (a <= 0 && b <= 0 && c <= 0) {
      console.log(cnt);
      return;
    }

    for (const perm of permutations) {
      const na = Math.max(0, a - perm[0]);
      const nb = Math.max(0, b - perm[1]);
      const nc = Math.max(0, c - perm[2]);

      if (!visited[na][nb][nc]) {
        visited[na][nb][nc] = true;
        queue.push([na, nb, nc, cnt + 1]);
      }
    }
  }
});
