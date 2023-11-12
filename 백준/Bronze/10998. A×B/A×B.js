let fs = require("fs")
let line = fs.readFileSync("/dev/stdin").toString().split(" ");

let num1 = parseInt(line[0])
let num2 = parseInt(line[1]);

console.log(num1*num2)