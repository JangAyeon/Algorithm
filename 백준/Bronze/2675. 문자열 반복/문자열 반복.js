let fs = require("fs")
let line = fs.readFileSync("/dev/stdin").toString().split("\n");

let T = Number(line[0])

function makeRepeat(s,n){
  let result =""
  for(let k=0;k<n;k++){result+=s;
  }
  return result
}

for (let i=1;i<=T;i++){
  let [n, arr] = line[i].split(" ")
  let str =""
  for(let s of arr){
 str+=makeRepeat(s, n);
  }
  console.log(str)
 
}