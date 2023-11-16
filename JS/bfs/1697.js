// 숨바꼭질

let fs = require("fs")
let line =fs.readFileSync("../input.txt").toString().split(" ")
let n = Number(line[0])
let k = Number(line[1])
const MAX = 100000*2;
let visited = new Array(MAX).fill(0);


function bfs(start,end, visited){
  let que =[]
  que.push(start)
  visited[start]=1
  while(que.length!=0){
    m = que.shift()
    for (let next of [m-1,m+1, m*2]){
      // 공간 벗어난 경우
      if(next<0 || next>=MAX){
        continue
      }
      // 처음 방문하는 경우
      if (visited[next] == 0) {
        //console.log(next);
        visited[next] = visited[m] + 1;
        que.push(next);
      }
      if(next==end){
        return visited[end]-1
      }

    }



    }

}

console.log(bfs(n,k,visited))