let  fs =require("fs")
let line = fs.readFileSync("/dev/stdin").toString().split(" ")

let num1 = Number(line[0].split("").reverse().join(""))
let num2 = Number(line[1]
  .split("")
  .reverse().join(""))
let answer = Math.max(num1, num2)
console.log(answer)