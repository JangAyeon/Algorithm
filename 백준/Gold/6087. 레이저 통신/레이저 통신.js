const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const dx = [0, -1, 0, 1]; // 서, 북, 동, 남
const dy = [-1, 0, 1, 0];

let w, h;
let board = [];
let pos = [];

rl.on("line", (line) => {
  if (!w || !h) {
    [w, h] = line.split(" ").map(Number);
  } else {
    board.push(line.split(""));
    let row = board.length - 1;
    for (let col = 0; col < w; col++) {
      if (board[row][col] === "C") {
        pos.push([row, col]);
      }
    }
  }
  if (board.length === h) {
    console.log(bfs(...pos[0], ...pos[1]));
    rl.close();
  }
});

function bfs(sx, sy, ex, ey) {
  const INF = 1e9;
  const queue = [];
  const visited = Array.from({ length: h }, () =>
    Array.from({ length: w }, () => Array(4).fill(INF))
  );

  for (let i = 0; i < 4; i++) {
    let nx = sx + dx[i],
        ny = sy + dy[i];
    if (nx >= 0 && nx < h && ny >= 0 && ny < w && board[nx][ny] !== "*") {
      queue.push([nx, ny, i]);
      visited[nx][ny][i] = 0;
    }
  }

  while (queue.length) {
    let [x, y, direct] = queue.shift();
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i],
          ny = y + dy[i];
      if (nx >= 0 && nx < h && ny >= 0 && ny < w && board[nx][ny] !== "*") {
        let cnt = visited[x][y][direct];
        if ((direct === 0 || direct === 2) && (i === 1 || i === 3)) cnt += 1;
        if ((direct === 1 || direct === 3) && (i === 0 || i === 2)) cnt += 1;

        if (visited[nx][ny][i] === INF) {
          visited[nx][ny][i] = cnt;
          queue.push([nx, ny, i]);
        } else if (visited[nx][ny][i] > cnt) {
          visited[nx][ny][i] = cnt;
          queue.push([nx, ny, i]);
        }
      }
    }
  }
  return Math.min(...visited[ex][ey]);
}
