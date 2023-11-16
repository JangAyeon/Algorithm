let fs = require("fs")
let line = fs.readFileSync("./input.txt").toString().split(" ")

let a = Number(line[0])
let b = Number(line[1]);
let c = Number(line[2]);
let arr = [a,b,c]
let result;
if (a==b && b==c){
  result = 10000+a*1000
}else if (a===b | a===c){
  result = a*100+1000
}
else if (b===c){
  result = b*100+1000
}
else{
result = Math.max(...arr)*100
}

console.log(result)