const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const lines = [];
rl.on("line", (line) => {
  lines.push(line.trim());
}).on("close", () => {
  let str_ = lines[0];
  const bomb = lines[1];
  const len = bomb.length;
  const stack = [];

  str_.split("").map((v) => {
    if (
      stack.slice(stack.length - len + 1, stack.length).join("") + v ===
      bomb
    ) {
      for (let i = 0; i < len - 1; i++) stack.pop();
    } else stack.push(v);
  });
  const answer = stack.length === 0 ? "FRULA" : stack.join("");
  console.log(answer);
});

/*
in:
AABCBABCBABCCABCC
ABC

out:
ABBCC
*/
