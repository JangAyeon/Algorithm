let fs = require("fs")
let line = fs.readFileSync("/dev/stdin").toString().split("\n")

let n = Number(line[0])

for(let j = 1;j<=n;j++){
  let result=""
  for (let k=1;k<=j;k++){
    result+="*"
  }
  console.log(result)
}