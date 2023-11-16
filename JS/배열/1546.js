let fs = require("fs")
let line = fs.readFileSync("../input.txt").toString().split("\n");

let n = Number(line[0]);
let arr = line[1].split(" ").map((x)=>Number(x))
let m = Math.max(...arr)
let score = []

for (let s of arr){
  score.push(s/m*100)
}
let total = score.reduce((a,b)=>a+b)
let cnt = arr.length
console.log(total/cnt)