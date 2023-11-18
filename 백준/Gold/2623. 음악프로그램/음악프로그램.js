const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const fs = require("fs");
let input = fs.readFileSync(filePath).toString().split("\n");

let [n, m] = input[0].split(" ").map(Number);
let arr = input.slice(1).map((x)=>x.split(" ").map(Number
  ))

function solution(N, M, input) {
  // 배열 graph에는 그래프의 정보를 저장한다.
  let graph = Array.from({ length: N + 1 }, () => []);
  // 배열 indegree에는 각 인덱스에 해당하는 정점으로 들어오는 간선의 개수를 저장한다.
  let indegree = Array.from({ length: N + 1 }, () => 0);
  for (let i = 0; i < M; i++) {
    let [n, ...list] = input[i];
    for (let j = 0; j < n - 1; j++) {
      graph[list[j]].push(list[j + 1]);
      indegree[list[j + 1]]++;
    }
  }
  let queue = [];
  let ans = [];
  for (let i = 1; i <= N; i++) {
    // 각 정점에 들어오는 간선의 개수가 없는 정점을 queue 배열에 추가한다.
    if (!indegree[i]) queue.push(i);
  }
  while (queue.length) {
    let cur = queue.shift();
    // 배열 queue에 정점을 꺼내 위상 정렬 결과를 저장하는 배열 ans에 추가한다.
    ans.push(cur);
    for (let next of graph[cur]) {
      // 정점 cur과 연결된 정점의 간선의 수를 1씩 감소시킨다.
      indegree[next]--;
      // 각 정점에 들어오는 간선의 개수가 없는 정점을 queue 배열에 추가한다.
      if (!indegree[next]) queue.push(next);
    }
  }
  // 순서를 정하는 것이 불가능한 경우에는 '0'을 출력한다.
  return ans.length === N ? ans.join("\n") : 0;
}


console.log(solution(n,m,arr))