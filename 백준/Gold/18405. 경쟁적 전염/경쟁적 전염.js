const fs = require("fs");

let graph = [];
let virus = [];
let que = [];
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
// Assuming the file content is in 'input.txt'
fs.readFile(filePath, "utf8", function (err, data) {
  if (err) {
    console.error(`Error reading file: ${err}`);
    return;
  }

  // Split the file content by newline
  const lines = data.split("\n");
  let lineIndex = 0;

  // Process the first line to get n and k
  let [n, k] = lines[lineIndex++].split(" ").map(Number);
  graph = lines
    .slice(lineIndex, lineIndex + n)
    .map((line) => line.split(" ").map(Number));
  lineIndex += n;

  // Process the second line to get s, x, and y
  let [s, x, y] = lines[lineIndex++].split(" ").map(Number);

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
        let nr = r + dr[idx],
          nc = c + dc[idx];
        if (nr < 0 || nr >= graph.length || nc < 0 || nc >= graph[0].length) {
          continue;
        }
        if (graph[nr][nc] === 0) {
          graph[nr][nc] = graph[r][c];
          que.push([nr, nc, time + 1]);
        }
      }
    }
  }

  bfs();
  console.log(graph[x - 1][y - 1]);
});
