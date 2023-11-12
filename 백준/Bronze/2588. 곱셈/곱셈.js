let fs = require("fs");
let line = fs.readFileSync("/dev/stdin").toString().split("\n");

let a = parseInt(line[0])
let b = line[1]

let num1 = parseInt(b[0])
let num2 = parseInt(b[1])
let num3 = parseInt(b[2])
let num4 = parseInt(b)

console.log(a*num3)
console.log(a * num2);
console.log(a * num1);
console.log(a*num4)