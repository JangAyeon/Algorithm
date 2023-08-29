// day7: 구름 찾기 깃발

const readline = require("readline");
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
let n;
let k;
rl.on("line", (line) => {
  input.push(line.trim());
  [n, k] = input[0].split(" ").map(Number);
  if (input.length == n + 1) {
    rl.close();
  }
});

const dr = [-1, +1, 0, 0, -1, -1, +1, +1];
const dc = [0, 0, -1, +1, -1, +1, -1, +1];
let zeros = [];
let graph = [];

function createGraph(input) {
  for (let i = 1; i < input.length; i++) {
    const temp = input[i].split(" ").map(Number);
    graph.push(temp);
  }
  return graph;
}

function getZeros() {
  for (let i = 0; i < graph.length; i++) {
    for (let j = 0; j < graph[i].length; j++) {
      if (graph[i][j] === 0) {
        zeros.push([i, j]);
      }
    }
  }
  return zeros;
}

function getCount() {
  answer = 0;
  for (let i = 0; i < zeros.length; i++) {
    const [r, c] = zeros[i];
    let count = 0;
    for (let j = 0; j < dr.length; j++) {
      const nr = r + dr[j];
      const nc = c + dc[j];
      if (0 <= nr && nr < n && 0 <= nc && nc < n) {
        if (graph[nr][nc] === 1) {
          count += 1;
        }
      }
    }
    if (count == k) {
      answer += 1;
    }
  }
  return answer;
}

rl.on("close", () => {
  graph = createGraph(input);
  zeros = getZeros();
  const answer = getCount();
  console.log(answer);
  process.exit();
});
