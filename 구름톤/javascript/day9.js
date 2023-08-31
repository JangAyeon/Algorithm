// day9: 폭탄 구현하기2

const readline = require("readline");
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
let n, k;
const graph = [];
const bombs = [];
const location = [];

dr = [0, -1, 1, 0, 0];
dc = [0, 0, 0, -1, 1];

// 땅 한변의 길이, 폭탄 떨어뜨릴 횟수
rl.on("line", (line) => {
  input.push(line.trim());
  [n, k] = input[0].split(" ").map(Number);
  if (input.length == n + k + 1) {
    createMaps();
    createQuery();
    rl.close();
  }
});

function createMaps() {
  for (let i = 1; i <= n; i++) {
    graph.push(input[i].split(" "));
  }
  // console.log(graph);
  for (let i = 1; i <= n; i++) {
    const temp = [];
    for (let j = 1; j <= n; j++) {
      temp.push(0);
    }
    bombs.push(temp);
  }
  //console.log(graph);
  //console.log(bomb);
}

function createQuery() {
  for (let i = 1; i <= k; i++) {
    const [r, c] = input[i + n].split(" ").map(Number);
    location.push([r - 1, c - 1]);
  }
  //console.log(location)
}

function game() {
  for (let i = 0; i < location.length; i++) {
    const [r, c] = location[i];
    for (let d = 0; d < 5; d++) {
      nr = r + dr[d];
      nc = c + dc[d];
      //console.log(nr,nc)
      if (0 <= nr && nr < n && 0 <= nc && nc < n && graph[nr][nc] !== "#") {
        //console.log(bombs)
        if (graph[nr][nc] === "@") {
          bombs[nr][nc] += 2;
        } else {
          bombs[nr][nc] += 1;
        }
      }
    }
  }
}

function getMax() {
  let bomb = 0;
  for (let i = 0; i < bombs.length; i++) {
    bomb = Math.max(bomb, Math.max(...bombs[i]));
  }

  return bomb;
}
rl.on("close", () => {
  game();
  // console.log(bombs);
  const answer = getMax();
  console.log(answer);
  process.exit();
});
