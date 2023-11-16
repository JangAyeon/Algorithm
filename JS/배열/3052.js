let fs = require("fs");
let line = fs.readFileSync("../input.txt").toString().split("\n");

let arr = line.map((x)=>Number(x))
let numSet = new Set();

for (let num of arr){
  numSet.add(num%42);
}

console.log(numSet.size)