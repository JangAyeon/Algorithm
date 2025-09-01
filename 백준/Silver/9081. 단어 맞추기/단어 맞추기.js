const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
/***
1. 주어진 문자열의 맨 뒤에서 시작해, 앞으로 가면서 처음으로 '감소하는 원소'의 위치를 idx1 에 저장한다.
2. 다시 주어진 문자열의 맨 뒤에서부터 시작해, 1에서 찾은 '감소하는 원소'보다 큰 원소를 처음으로 만나면 그 원소의 위치를 idx2에 저장한다.
3. 1에서 찾은 '감소하는 원소'와 2에서 찾은 '큰 원소'를 swap 해준다. 
4. idx1 위치 이후에 있는 모든 원소들을 오름차순으로 정렬한다. 
***/
function nextPermutation(arr) {
  let i = arr.length - 2;
  while (i >= 0 && arr[i] >= arr[i + 1]) i--;

  if (i < 0) return false; // 마지막 순열

  let j = arr.length - 1;
  while (arr[j] <= arr[i]) j--;

  // swap
  [arr[i], arr[j]] = [arr[j], arr[i]];

  // reverse 뒤쪽
  let left = i + 1,
    right = arr.length - 1;
  while (left < right) {
    [arr[left], arr[right]] = [arr[right], arr[left]];
    left++;
    right--;
  }
  return true;
}

function solution(word) {
  const arr = word.split("");
  const hasNext = nextPermutation(arr);
  if (!hasNext) return word;
  return arr.join("");
}

rl.on("line", (line) => lines.push(line)).on("close", () => {
  let T = Number(lines.shift());
  while (T--) {
    console.log(solution(lines.shift()));
  }
});
