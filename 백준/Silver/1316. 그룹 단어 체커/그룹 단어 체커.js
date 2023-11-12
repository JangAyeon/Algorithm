let fs = require("fs")
let line = fs.readFileSync("/dev/stdin").toString().split("\n");

let T = Number(line[0])
let answer = 0

function isValid(str){
  let prev=""
  let chSet= new Set()
for(let s of str){

  if (prev!=s){
    if (chSet.has(s)){      return false
    }
    else{
      chSet.add(s)
      prev=s
    }
  }
  
}

return true
}
for (let i=1; i<=T;i++){
  if(isValid(line[i])){

    answer+=1
  }
}

console.log(answer)