let fs =  require("fs")
let input = fs.readFileSync("../input.txt").toString().split("\n")

let n = Number(input[0])
let arr= input[1].split(" ").map(Number)
arr.sort((a,b)=>a-b)
//console.log(n, arr);

let answer=0
for(let i =0;i<n;i++){
  let totalArray = arr.slice(0,i+1)
  let temp = totalArray.reduce((x,y)=>x+y,0)
  answer+=temp

}

console.log(answer)