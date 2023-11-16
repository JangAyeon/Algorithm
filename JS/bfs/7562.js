// 나이트의 이동

let fs = require("fs")
let line = fs.readFileSync("../input.txt").toString().split("\n")

let T = Number(line[0])
let dr=[-2,-2,-1,-1,+1,+1,+2,+2]
let dc=[-1,+1,-2,+2,-2,+2,-1,+1]

function createVisited(n){
  // visitedrr[n][n] (0으로 초기화하여 생성)
  let visited = Array.from(Array(n), () => Array(n).fill(0));
  
  return visited;
}

function bfs( n,start,end,visited){
  let que = []
  let [r,c] =start
  que.push([r,c])
  visited[r][c]=1
  while(que.length!=0){
    [r,c] = que.shift()
    for (let idx = 0; idx<8;idx++){
      let nr = r+dr[idx]
      let nc = c+dc[idx]
      // 범위 벗어남 OR 방문한 곳인 경우
if (nr < 0 || nr >= n || nc < 0 || nc >= n) continue; // 공간을 벗어난 경우 무시
      if(visited[nr][nc]==0){
      visited[nr][nc] = visited[r][c] + 1;
      que.push([nr, nc]);
      }
      


    }
  }

  return visited[end[0]][end[1]]
}

for (let i=1; i<=T*3;i+=3){
  let n = Number(line[i]);
  let start = line[i + 1].split(" ").map((x) => Number(x));
  let end = line[i + 2].split(" ").map((x) => Number(x));
  let visited = createVisited(n);
  //console.log(n, start, end)
  //console.log(visited)
  console.log(bfs(n, start, end, visited)-1);
}