// https://www.acmicpc.net/problem/2750

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);

let arr = [];

for (let i = 1; i <= n; i++) {
  arr.push(Number(input[i]));
}

arr.sort((x, y) => x - y);

arr.forEach((x) => console.log(x));
