const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  const word = input[0];
  const bomb = input[1];
  const stack = [];

  for (let i = 0; i < word.length; i++) {
    stack.push(word[i]);
    // 제거한 후에 또 폭탄이 생길 수 있으므로 반복
    outer: while (stack.length >= bomb.length) {
      for (let j = 0; j < bomb.length; j++) {
        if (stack[stack.length - 1 - j] !== bomb[bomb.length - 1 - j]) {
          break outer; // 없으면 아예 종료 (라벨을 활용해 바깥의 루프를 종료)
        }
      }
      // 같네?! -> 스택에서 제거
      for (let j = 0; j < bomb.length; j++) {
        stack.pop();
      }
    }
  }
  if (!stack.length) console.log("FRULA");
  else console.log(stack.join(""));
});