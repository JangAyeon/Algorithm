let fs = require("fs")
let input = fs.readFileSync("/dev/stdin").toString().split(" ").map((x)=>Number(x))
let [n,m] = input
//console.log(n,m)
const MAX_ = 1e9


function calc(num,cmd){
  if (cmd=="+"){
    return num+num
  }
  if(cmd=="/"){
    return Math.floor(num/num)
  }
  if(cmd=="*"  ){
    return num*num
  }
  if(cmd=="-"){
    return num-num
  }
}

const cmds = ['*', '+', '-', '/' ];
function bfs(num){
  let que = [[num, []]];
  let visited=[num]
  while (que.length !=0){
    [num, process]= que.shift()
    // console.log(num, process)
    for(let cmd of cmds){
      if (num==0 && cmd=="/"){
        continue
      }
      else{
        x=calc(num, cmd)
        
        if (x==m){
          return process+[cmd]
        }
        else if(x<MAX_ && !(visited.includes(x))){
          que.push([x, process+[cmd]])
          visited.push(x)
        }
      }
    }
  }
  return []
  

}

if (n==m){
  console.log(0)
}
else{
  const result = bfs(n)
  if (result.length==0){
    console.log(-1)
  }
  else{
    console.log(result)
  }

}