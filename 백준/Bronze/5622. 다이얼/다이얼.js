const filePath=process.platform==="linux"?"/dev/stdin":"../input.txt"
const fs = require("fs")
const input = fs.readFileSync(filePath).toString().split("\n")

const arr=  input[0].split("")
const nums = [[],["A","B","C"],["D","E","F"],["G","H","I"],["J","K","L"],["M","N","O"],["P","Q","R","S"],["T","U","V"],["W","X","Y","Z"]]




let answer=0
for (let s of arr){
  for(let row of nums){
    if (row.includes(s)){
      //console.log(nums.indexOf(row)+2)
      answer+=nums.indexOf(row)+2
    }
  }
}

console.log(answer)