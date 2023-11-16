let fs = require("fs")
let input = fs.readFileSync("../input.txt").toString().split("\n")

let n = Number(input[0])
let arr = input[1].split(" ").map((x)=>Number(x))
let sortedArr = [...new Set(arr)].sort((a, b) => (a - b));


let sortMap = new Map()
for (let i=0;i<sortedArr.length;i++){
  sortMap.set(sortedArr[i],i)
}

let answer=""
arr.forEach((x)=>answer+=`${sortMap.get(x)} `)
console.log(answer)