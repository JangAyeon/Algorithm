// https://www.acmicpc.net/problem/1697
let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .split(" ")
  .map((x) => Number(x));

let [n,k] = input
const MAX_ = 100000;
const INF = Number.MAX_SAFE_INTEGER;
const dist = Array.from({length:MAX_+1},(v,i)=>INF)


function loc(x){
  const location = [x+1, x-1, x*2]
  const res = location.filter((el) => 0 <= el && el <= MAX_);
  return res
}

function bfs(start){
  const que = [start]
  dist[start] = 0
  while (que.length>0){
    const curr = que.shift()
    for(const next_ of loc(curr)){
      if (dist[next_] > dist[curr] + 1) {
        dist[next_] = dist[curr] + 1;

        que.push(next_);
      }
    }
  }
}

bfs(n)
console.log(dist[k])