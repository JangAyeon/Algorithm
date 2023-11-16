let fs = require("fs")
let line = fs.readFileSync("../input.txt").toString().split("\n")


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
      // 이전에 방문했는데 상태가 다른 경우
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
  // 입력받은 line에서 인덱스로 접근해야 시간 초과 발생하지 않는다
  // 배열에서 요소 빼는 메서드 사용하는 경우 시간초과 발생 
  [v, e] = line[idx].split(" ").map((x) => Number(x));
  // 상태 : (초기화 :-1, 상태: 0 또는 1)
  visited = Array(v + 1).fill(-1);
  // 그래프 생성
  graph = Array.from(Array(v + 1), () => new Array());
  for (let j = 1; j <= e; j++) {
    [x1, x2] = line[idx + j].split(" ").map((x) => Number(x));
    graph[x1].push(x2);
    graph[x2].push(x1);
  }
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