let fs = require("fs")
let line = fs.readFileSync("/dev/stdin").toString().split("\n")


let T = Number(line[0])
let idx=1

function bfs(start){
  let que = [start]
  visited[start]=0
  while (que.length!=0){
    node = que.shift()
    state = (visited[node]+1)%2
    for (let next_ of graph[node]){
      // console.log(node,next_,state, visited[node], visited[next_],visited)
      // 최초 방문
      if (visited[next_]==-1){
        visited[next_]=state
        que.push(next_)
      }
      else if(visited[next_]!=state){
        return false
      }

    }

  }

  return true

}
let visited;
let graph;

while(T--){
  [v, e] = line[idx].split(" ").map((x) => Number(x));
  // 상태
  visited = Array(v + 1).fill(-1);
  // 그래프 생성
  graph = Array.from(Array(v + 1), () => new Array());
  for (let j = 1; j <= e; j++) {
    [x1, x2] = line[idx + j].split(" ").map((x) => Number(x));
    graph[x1].push(x2);
    graph[x2].push(x1);
  }
  // console.log(graph, visited);
  let answer = "YES";
  for (let start = 1; start <= v; start++) {
    // 최초 방문
    if (visited[start] == -1) {
      if (bfs(start) == false) {
        answer = "NO";
        break;
      }
    }
  }
  idx += e + 1; // 다음 테스트 케이스로 이동
  console.log(answer);
}