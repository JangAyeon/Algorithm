let fs = require("fs");
let line = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(line[0])
let arr = line[1].split(" ").map(Number)

let max_=Math.max(...arr)
let min_=Math.min(...arr)

console.log(min_,max_ )