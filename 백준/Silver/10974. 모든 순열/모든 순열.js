let fs = require("fs")
let input=fs.readFileSync("/dev/stdin").toString().split("\n")

let n =Number(input[0])
let arr = new Array(n).fill(0).map((_, idx)=>idx+1)
let visited=new Array(n).fill(false)
let select=[]
let answer=""

function dfs(idx){
  if(idx==n){
    answer+=`${select.join(" ")}\n`
    return
  }
  for(let i=0;i<n;i++){
    if(visited[i]==true){continue}
    visited[i]=true
    select.push(arr[i])
    dfs(idx+1)
    visited[i]=false
    select.pop()
  }
}

dfs(0)
console.log(answer)