let fs = require("fs")
let input = fs.readFileSync("/dev/stdin").toString().split("\n")

let [n,m]=input[0].split(" ").map(Number) 
let arr = new Array(n).fill(0).map((item, idx)=>idx+1)
let visited = new Array(n).fill(false)

let answer=""

function dfs(idx){
  if(idx==m){
    // console.log("답 추가", lst)
    answer+=`${lst.join(" ")}\n`
    return
  }



  for(let i=0;i<n;i++){
    // 이미 방문한 경우
    if(visited[i]){continue}
    // 추가하기
    lst.push(arr[i])
    visited[i]=true
    dfs(idx+1)
    lst.pop()
    visited[i]=false



  }



}
let lst=[]
dfs(0)
console.log(answer)