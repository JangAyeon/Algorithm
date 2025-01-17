const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const inputs = fs
  .readFileSync(path)
  .toString()
  .trim()
  .split("\n")
  .map((it) => it.split(" ").map(Number));

const [n, e] = inputs[0];
const [v1, v2] = inputs.at(-1);
const graph = Array.from(Array(n + 1), () => []);
const NONE = -1;

for (let i = 1; i <= e; i++) {
  const [s, e, c] = inputs[i];
  graph[s].push([e, c]);
  graph[e].push([s, c]);
}

const getMinNode = (distance, visited) => {
  let minNode = NONE;
  let minDistance = Infinity;

  for (let i = 1; i <= n; i++) {
    if (!visited[i] && distance[i] < minDistance) {
      minNode = i;
      minDistance = distance[i];
    }
  }

  return minNode;
};

const dijkstra = (start) => {
  const distance = Array(n + 1).fill(Infinity);
  const visited = Array(n + 1).fill(false);

  distance[start] = 0;

  while (true) {
    const minNode = getMinNode(distance, visited);

    if (minNode === NONE) break;
    visited[minNode] = true;

    for (const [nE, nC] of graph[minNode]) {
      if (distance[minNode] + nC < distance[nE]) {
        distance[nE] = distance[minNode] + nC;
      }
    }
  }
  return distance;
};

const start1 = dijkstra(1);
const startV1 = dijkstra(v1);
const startV2 = dijkstra(v2);

const ans = Math.min(
  start1[v1] + startV1[v2] + startV2[n],
  start1[v2] + startV2[v1] + startV1[n]
);

console.log(ans === Infinity ? -1 : ans);
