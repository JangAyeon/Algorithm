// https://www.acmicpc.net/problem/2751

let fs = require("fs");
let input = fs.readFileSync("../input.txt").toString().split("\n");

let n = Number(input[0]);

let arr = [];

for (let i = 1; i <= n; i++) {
  arr.push(Number(input[i]));
}

arr.sort((x, y) => x - y);

let answer = "";
arr.forEach((x) => (answer += `${x}\n`));
console.log(answer);
