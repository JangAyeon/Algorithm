// day 4: 완벽한 햄버거 만들기

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

// 맛의 정도가 가장 높은 재료 기준으로 위와 아래로 햄버거 나누기
function split(n, arr) {
  const idx = arr.indexOf(Math.max(...arr));
  return idx;
}

// 위에서 아래로 갈수록 재료 맛 정도가 같거나 감소하는지 판별
function isValid(arr, sortedArr, n) {
  for (let i = 0; i < arr.length; i++) {
    //console.log(arr[i], sortedArr[i])
    if (arr[i] == sortedArr[i] && arr[i] <= n) {
      continue;
    } else {
      return false;
    }
  }
  return true;
}

// 햄버거 재료 합 구하기
function getSum(arr) {
  let answer = 0;
  for (let idx = 0; idx < arr.length; idx++) {
    answer += arr[idx];
  }
  return answer;
}

// 올바른 햄버거 여부에 따른 재료 합 또는 0 반환
function isComplete(leftBool, rightBool, arr) {
  if (leftBool && rightBool) {
    // 배열 전체 함
    return getSum(arr);
  } else {
    return 0;
  }
}

rl.on("close", () => {
  const n = input[0];
  const arr = input[1].split(" ").map(Number);

  // 맛의 정도가 가장 높은 재료 기준으로 나누기
  const idx = split(n, arr);

  // 나눈 기준 왼쪽(아래)에 속하는 배열
  const left = arr.slice(0, idx);
  const leftSort = [...left].sort((a, b) => a - b); // 오름차순 - 올바르게 정렬된 경우

  // 나눈 기준 오른쪽(위)에 속하는 배열
  const right = arr.slice(idx + 1);
  const rightSort = [...right].sort((a, b) => b - a); // 내림차순 - 올바르게 정렬된 경우

  // 각 오른쪽과 왼쪽에 대해 재료 맛의 정도가 올바르게 나열되었는지 판별 결과
  const rightBool = isValid(right, rightSort, arr[idx]);
  const leftBool = isValid(left, leftSort, arr[idx]);

  // 판별 결과에 따른 답 반환
  const answer = isComplete(rightBool, leftBool, arr);

  console.log(answer);

  process.exit();
});
