let fs = require("fs")
let line = fs.readFileSync("/dev/stdin").toString().split("\n")
let n = Number(line[0])

console.log(n*(n+1)/2)