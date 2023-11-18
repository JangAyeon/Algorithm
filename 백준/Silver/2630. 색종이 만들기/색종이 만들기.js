const filePath = process.platform=="linux"?"/dev/stdin":"../input.txt"
const fs = require("fs")
const input = fs.readFileSync(filePath).toString().split("\n");

const n=Number(input[0])
const graph=input.slice(1).map((v)=>v.split(" ").map(Number))

let bCnt=0
let wCnt=0




function recursion(n,x,y){

  let result=0
  for(let dx=0;dx<n;dx++){
    for(let dy=0;dy<n;dy++){
      result+=graph[x+dx][y+dy]
    }
  }

  if(result==0){
    wCnt+=1
    return
  }
  else if(result==n*n){
    bCnt+=1}
  else{
    n=n/2

    recursion(n,x,y)
    recursion(n,x+n,y)
    recursion(n,x,y+n)
    recursion(n,x+n,y+n)
  }
}

recursion(n,0,0)
console.log(wCnt)
console.log(bCnt)