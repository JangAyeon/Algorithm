// day6: 문자열 나누기

const readline = require("readline");
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", (line) => {
  input.push(line.trim());
  if (input.length == 2) {
    rl.close();
  }
});

// 문자열 3개의 부분 문자열로 나누기
function splitPoint(string) {
  const split = [];
  for (let i = 1; i < string.length; i++) {
    for (let j = i + 1; j < string.length; j++) {
      const first = string.slice(0, i);
      const second = string.slice(i, j);
      const third = string.slice(j);
      split.push([first, second, third]);
    }
  }
  return split;
}

// 부분 문자열 중복 제거하고 사전 순서로 정렬한 결과
function getSplitDic(arr) {
  // 1. 평면화로 이중 리스트 -> 단순 1차원 리스트로 변환
  // 2. new Set으로 중복 제거 -> spread 연산자로 배열 얕은 복사
  // 3. sort()를 통한 정렬
  return [...new Set(arr.flat())].sort();
}

// 부분 문자열에 대한 점수 구하기
function getScore(splitedString, splitedDic) {
  //console.log(splitedDic, splitedString)
  let scores = [];
  for (let i = 0; i < splitedString.length; i++) {
    let score = 0;
    for (let j = 0; j < splitedString[i].length; j++) {
      //console.log(splitedString[i][j]);
      //console.log(splitedDic.indexOf(splitedString[i][j])+1);
      score += splitedDic.indexOf(splitedString[i][j]) + 1;
      //console.log(score);
    }
    scores.push(score);
  }
  //console.log(scores);
  return scores;
}

rl.on("close", () => {
  const splitedString = splitPoint(input[1]);
  const splitedDic = getSplitDic(splitedString);
  const scores = getScore(splitedString, splitedDic);

  // 최대 점수 구하기
  const answer = Math.max(...scores);
  console.log(answer);
});
