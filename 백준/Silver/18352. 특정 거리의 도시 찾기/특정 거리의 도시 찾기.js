const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let lines = fs.readFileSync(filePath).toString().trim().split("\n");

// 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가
let index = 0;
let [n,m,k,x] = lines[index++].split(" ").map(Number)
let graph = Array.from({length:n+1}, ()=>[])
let dist = Array.from({length:n+1}, ()=>Number.MAX_SAFE_INTEGER)
let answer = []


for(let idx=1;idx<=m;idx++){
  let [a, b] = lines[idx].split(" ").map(Number)
  graph[a].push(b)
}

function bfs(start){
  const que = [start]
  dist[start] = 0
  while (que.length){
    const curr = que.shift()
    if (dist[curr]==k){
        answer.push(curr)
        continue
    }
      for (let next_ of graph[curr]) {
       
        if (dist[next_] > dist[curr] + 1) {
          
          dist[next_] = dist[curr] + 1;
          que.push(next_);
        }
      }
  }

}

bfs(x)
answer = answer.length?answer:[-1]
answer.sort((a,b)=>a-b)

for(let v of answer){
  console.log(v)
}