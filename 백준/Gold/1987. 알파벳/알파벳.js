// https://tesseractjh.tistory.com/191
// https://velog.io/@jiyaho/%EB%B0%B1%EC%A4%80-1987-%EC%95%8C%ED%8C%8C%EB%B2%B3-Node.js-DFS-%ED%92%80%EC%9D%B4

const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(filePath).toString().trim().split('\n');
const [R, C] = input.shift().split(' ').map(Number);
const board = input.map((v) => v.split(''));
const ds = [[0, 1], [0, -1], [-1, 0], [1, 0]]; // 인접한 좌우상하 x,y좌표
const visit = Array(26).fill(false); // 방문 배열 길이 = 알파벳 개수 26개
const item = (x, y) => board[x][y].charCodeAt() - 65; // 보드의 해당 알파벳을 정수로 변환
let answer=0
const dfs = (x, y, depth) => {
  answer = Math.max(depth, answer); // 말이 지나간 경로 중 최대값을 담을 변수
  visit[item(x, y)] = true; // 현재 위치 방문 처리

  // 인접한 네 방향 탐색할 반복문
  for (let i = 0; i < 4; i++) {
    const nx = x + ds[i][0];
    const ny = y + ds[i][1];
	
	// 다음 위치가 보드 범위를 벗어나지 않았고, 방문하지 않았다면,
    if (nx >= 0 && nx < R && ny >= 0 && ny < C && !visit[item(nx, ny)]) {
	  // 기존까지 dfs실행 후 저장된 최대값과 다음 dfs 결과값 비교하여 큰 값을 저장, 카운트 증가 
      dfs(nx, ny, depth + 1);
    }
  }
  visit[item(x, y)] = false; // 방문 배열 초기화
};

// 0,0 좌표에서 시작, 말이 지나가는 칸의 수(첫 번째 칸도 포함하므로 초기값 1)
dfs(0, 0, 1);
console.log(answer)