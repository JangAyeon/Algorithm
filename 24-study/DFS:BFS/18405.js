

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let lines = fs.readFileSync(filePath).toString().trim().split("\n")


let graph = [];
let virus = [];
let que = [];


// Process the first line to get n and k
const [n, k] = lines[0].split(" ").map(Number);
graph = lines
  .slice(1, 1 + n)
  .map((line) => line.split(" ").map(Number));


// Process the second line to get s, x, and y
const [s, x, y] = lines[lines.length-1].split(" ").map(Number);

// Process the virus data
for (let r = 0; r < graph.length; r++) {
  for (let c = 0; c < graph[0].length; c++) {
    if (graph[r][c]) {
      virus.push([graph[r][c], r, c]);
    }
  }
}
virus.sort((a, b) => a[0] - b[0]);

// Initialize the queue with virus data
  for (let v of virus) {
    que.push([v[1], v[2], 0]);
  }

// The rest of the code remains the same
const dr = [-1, 1, 0, 0];
const dc = [0, 0, -1, 1];

  function bfs() {
    while (que.length) {
      let [r, c, time] = que.shift();

      if (time === s) {
        continue;
      }

      for (let idx = 0; idx < 4; idx++) {
        const nr = r + dr[idx];
        const nc = c + dc[idx];
        if (!(0<=nc && nc<n)||(!(0<=nr && nr<n))) {
          continue;
        }
        if (!graph[nr][nc]) {
          graph[nr][nc] = graph[r][c];
          que.push([nr, nc, time + 1]);
        }
      }
    }
  }

bfs();
console.log(graph[x - 1][y - 1]);