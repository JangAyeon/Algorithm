let fs = require("fs")
let input = fs.readFileSync("../input.txt").toString().split("\n")

let minus = input[0].split("-")
//console.log(minus)
let answer=0

for (let i=0;i<minus.length;i++){
let temp=minus[i].split("+").map(Number).reduce((x,y)=>x+y,0)

if (i==0){
  answer+=temp
}
else{
  answer-=temp
}
}

console.log(answer)