const readline = require("readline");
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", (line) => {
  input.push(line.trim());
  if (input.length === Number(input[0]) + 1) {
    rl.close();
  }
});
const op = [];
const num = [];
let n;
function getCommands(input) {
  n = Number(input[0]);
  for (let i = 1; i < n + 1; i++) {
    const cmds = input[i].split(" ");
    op.push(cmds[1]);
    num.push([Number(cmds[0]), Number(cmds[2])]);
    // console.log(op, num);
  }
}

function getAnswer() {
  let answer = 0;
  for (let i = 0; i < n; i++) {
    if (op[i] === "+") {
      answer += num[i][0] + num[i][1];
    } else if (op[i] === "-") {
      answer += num[i][0] - num[i][1];
    } else if (op[i] === "*") {
      answer += num[i][0] * num[i][1];
    } else if (op[i] === "/") {
      answer += Math.floor(num[i][0] / num[i][1]);
    }
  }
  return answer;
}

rl.on("close", () => {
  getCommands(input);
  const answer = getAnswer();
  console.log(answer);
  process.exit();
});
