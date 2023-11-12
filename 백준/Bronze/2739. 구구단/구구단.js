let fs = require("fs")
let line = fs.readFileSync("/dev/stdin").toString().split("\n")

let n = Number(line[0])

for(let j = 1;j<10;j++){
  console.log(`${n} * ${j} = ${n*j}`)
}