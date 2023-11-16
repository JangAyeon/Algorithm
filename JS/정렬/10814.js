let fs = require("fs")
let input = fs.readFileSync("../input.txt").toString().split("\n")

let n = Number(input[0])
let arr=[]

for(let i =1;i<=n;i++){
  let [age, name] = input[i].split(" ")
  arr.push([Number(age), name])
}


arr.sort((x,y)=>x[0]-y[0])
arr.forEach((x)=> console.log(x.join(" ")))