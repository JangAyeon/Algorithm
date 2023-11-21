const fs = require("fs");
const filePath = process.platform==="linux"?"/dev/stdin":"../input.txt"
const input = fs.readFileSync(filePath).toString().split("\n");


const n = Number(input[0])
let que = []
let graph = Array.from({length:n+1},()=>[]) // 연결 정보
let need = Array.from(Array(n+1), () => Array(n+1).fill(0)); // 필요 정보
let degree = Array(n+1).fill(0)
const m = Number(input[1])
//console.log(graph,need, degree)


for (let i=0;i<m;i++){ // 진입 차수
  const [a,b,c] = input[2+i].split(" ").map(Number)
  graph[b].push([a,c])
  degree[a]+=1
  
}
//console.log("graph",graph)
for(let i=1;i<n+1;i++){
  if(degree[i]==0){
    que.push(i)
  }
}


while(que.length!=0){
  const now = que.shift()
  for(let node of graph[now]){
    const next_ =node[0]
    const next_need = node[1]
    let count = need[now].filter((x)=>x===0).length
    //console.log("count", count, next_, next_need)

    // 기본 부품
    if(count==n+1){
      need[next_][now]+=next_need
    }
    else{
      for (let i=1;i<n+1;i++){
        need[next_][i]+=next_need*need[now][i]
      }
    }
    degree[next_]-=1
    if(degree[next_]==0){
      que.push(next_)
    }
  }
}

//console.log(need[n])

for(let i=0;i<n+1;i++){
  if(need[n][i]>0){
    console.log(i, need[n][i])
  }
}