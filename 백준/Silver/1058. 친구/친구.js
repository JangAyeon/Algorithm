const fs = require("fs");
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
const N = parseInt(input[0]);
const relation = input.slice(1).map((r) => r.split(""));
const [ROW, COL] = [N, N];
const INF = Number.MAX_SAFE_INTEGER;

function getArr(r, c) {
  return Array.from(Array(r), () => Array(c).fill(INF));
}

function floyd(arr) {
  for (let d = 0; d < ROW; d++) {
    for (let i = 0; i < ROW; i++) {
      for (let j = 0; j < COL; j++) {
        const cost = arr[i][d] + arr[d][j];
        if (arr[i][j] > cost) {
          arr[i][j] = cost;
        }
      }
    }
  }
  return arr;
}

function init(arr) {
  for (let i = 0; i < ROW; i++) {
    for (let j = 0; j < COL; j++) {
      if (i == j) {
        arr[i][j] = 0;
      } else if (relation[i][j] == "Y") {
        arr[i][j] = 1;
      }
    }
  }
  return arr;
}

function getAnswer(arr) {
  return arr.reduce((a, b) => Math.max(a, b));
}

function getCount(arr) {
  const count = Array(N).fill(0);
  for (let i = 0; i < ROW; i++) {
    for (let j = 0; j < COL; j++) {
      if (arr[i][j] <= 2 && i != j) {
        //console.log(arr[i][j]);
        count[i] += 1;
      }
    }
  }
  return count;
}

function solution() {
  const dist = init(getArr(ROW, COL));
  const arr = floyd(dist, ROW, COL);
  const count = getCount(arr);
  const answer = getAnswer(count);
  console.log(answer);
}

solution();
