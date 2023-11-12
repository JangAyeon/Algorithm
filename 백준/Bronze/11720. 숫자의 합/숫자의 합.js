let fs = require("fs")
let line = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(line[0])
let arr = line[1].split("").map((x)=>Number(x))
let total = arr.reduce((a,b)=>a+b)
console.log(total)