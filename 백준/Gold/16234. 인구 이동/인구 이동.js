const filePath = process.platform==="linux"?"/dev/stdin":"../input.txt"
const fs = require("fs")
const input = fs.readFileSync(filePath).toString().split("\n")

// 인구 차이가 l명 이상 r명 이하 => 국경선 공유
const [N,L,R] = input[0].split(" ").map(Number)
let graph = input.slice(1).map(x=>x.split(" ").map(Number))


const dr = [-1,1,0,0]
const dc = [0,0,-1,1]
let answer =0 

// 범위 체크 함수
const isRange = (r, c) => {
  if (r >= 0 && c >= 0 && r < N && c < N) return true;
  return false;
};



function bfs(r,c,visited){

  let que=[[r,c]] // 탐색 큐
  let unit=[[r,c]] // 연합 모음
  visited[r][c] = true; // 방문 처리 
  let population = graph[r][c] // 연합 인원 수 합
  while (que.length) {
    const [curR, curC] = que.shift();

    for (let i = 0; i < 4; i++) {
      const nr = curR + dr[i];
      const nc = curC + dc[i];

      if (isRange(nr, nc) && !visited[nr][nc]) {
        // 4방위를 탐색하며 조건에 맞는 다음좌표와의 인구 값 차이 구하기
        const difference = Math.abs(graph[curR][curC] - graph[nr][nc]);

        // 인구 값 차이가 조건에 맞다면
        if (difference >= L && difference <= R) {
          visited[nr][nc] = true; // 방문 체크하고
          que.push([nr, nc]); // 다음 탐색 좌표에 넣고
          unit.push([nr, nc]); // 현재 턴에서 연합에 넣음
          population += graph[nr][nc]; // 연합의 총 인원 수 증가
        }
      }
    }
  }

  if(unit.length>1){
    unit.forEach(([r,c])=>{
      graph[r][c]=Math.floor(population/unit.length)
    })
  }
  return unit.length
 
}


while (true){
  let visited = Array.from(Array(N), () =>
    Array(N).fill(false)
  );


  let unitFormed = false
  for (let r= 0; r < N ; r++) {
    for(let c=0;c<N;c++){
    if (!visited[r][c]) {
      const unitCount = bfs(r, c, visited);
      if (unitCount>1) {
        unitFormed = true;
      }
    }
     
    }
  }

  if (!unitFormed){break}
  answer++;






}



console.log(answer)


/***
 * 
4 1 9
96 93 74 30
60 90 65 96
5 27 17 98
10 41 46 20
correct: 1
*
 */

/***
 * 
5 1 5
88 27 34 84 9
40 91 11 30 81
2 88 65 26 75
75 66 16 14 28
89 10 5 30 75
correct: 1
*
 */