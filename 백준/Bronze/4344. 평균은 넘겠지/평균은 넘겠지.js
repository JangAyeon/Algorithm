let fs = require("fs")
let line = fs.readFileSync("/dev/stdin").toString().split("\n")

let n = Number(line[0])

function getCount(scores, avg){
  let count =0

  for(let s of scores){
    if (s>avg){
      count+=1
      }
  }
  return count
}

for (let i = 1;i<=n;i++){
  let arr = line[i]
    .split(" ")
    .map((x) => Number(x)).slice(1,)
  let total = arr.reduce((a,b)=>a+b)
  let cnt = arr.length
  let avg = total/cnt
  let student = getCount(arr, avg)
  console.log((student/cnt*100).toFixed(3)+"%")
}