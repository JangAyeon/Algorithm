let fs = require("fs");
let line = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(line[0]);
let arr = line[1].split(" ").map((x) => Number(x));

/* 방법 1 
let min_ = arr.reduce((a, b) => Math.min(a, b));
let max_ = arr.reduce((a, b) => Math.max(a, b));
*/

// 방법 2
let max_ = Math.max(...arr);
let min_ = Math.min(...arr);

console.log(min_, max_);
