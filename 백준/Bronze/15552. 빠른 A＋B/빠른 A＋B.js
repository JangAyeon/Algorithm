let fs = require("fs");
let line = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(line[0]);
let answer="";

for (let j = 1; j <= n; j++) {
  let [a,b] = line[j].split(" ").map(Number);
  answer+=(a+b)+"\n"
}

console.log(answer)