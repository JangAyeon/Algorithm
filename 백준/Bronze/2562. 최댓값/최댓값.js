let fs =require("fs")
//let line = fs.readFileSync("../input.txt").toString().split("\n");
let line = fs.readFileSync("/dev/stdin").toString().split("\n")

// 서로 다른 자연수
let arr = line.map((x)=>Number(x));
let max_ = Math.max(...arr)
let index = arr.indexOf(max_)
console.log(max_)
console.log(index+1)