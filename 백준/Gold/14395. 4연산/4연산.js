const fs = require("fs")
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const inputs = fs.readFileSync(filePath).toString().split("\n")
const [n,m] = inputs[0].split(" ").map(Number)
// console.log(n,m)

const MAX_ = 10**9
const visited = []
const ans = []
const cmds=["*","+","-","/"]
cmds.sort()


function calc(num, cmd){
  if (cmd==="+"){
    return num+num
  }
  else if (cmd==="-"){
    return num-num
  }
  else if (cmd==="*"){
    return num * num
  }
  else if(cmd=="/"){
    return num/num
  }
}


function bfs(){
  const que = [[n, []]]
  while(que.length>0){
    const [num,process] = que.shift()
    
    for(let cmd of cmds){
      //console.log(num, process, cmd, cmds);
      if (num===0 && cmd==="/"){
        continue
      }
      x = calc(num, cmd)

      // 목표 수 도달한 경우
      if (x===m){
        // console.log([...process, cmd]);
        ans.push([...process, cmd])
        return
      }
      if((x<=MAX_)&&(!visited.includes(x))){
        // console.log([...process, cmd]);
        que.push([x, [...process, cmd]])
        visited.push(x)
      }
    }
  }
}
bfs()
if (n===m){
  console.log(0)
}
else{
  if(ans.length===0){
    console.log(-1)
  }
  else{
    ans.sort()
    console.log(ans[0].join(""));
  }
}
