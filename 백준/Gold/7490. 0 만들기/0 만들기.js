let fs =require("fs")
let input =fs.readFileSync("/dev/stdin").toString().split("\n")

let T = Number(input[0])

let cmds=["+","-"," "]


function getCalc(ops){
  let result=""

  for(let i=0;i<arr.length-1;i++){
    result+=`${arr[i]}${ops[i]}`
  }
  result+=`${arr[arr.length-1]}`

 return result

}



function dfs(idx, ops){
    if (idx== n-1) {
        // 연산자 다  선택된 상태임
        let operation = getCalc(ops)
        let result = eval(operation.split(" ").join(""));
        if (result===0){answer.push(operation)}
      return;
    }

for(let cmd of cmds){
  ops.push(cmd)
  dfs(idx+1, ops)
  ops.pop()
}

}
for(let t=1;t<=T;t++){
  answer=[]
  n = Number(input[t])
  arr = new Array(n).fill(0).map((_,idx)=>idx+1)
  let ops=[]

  // console.log(n,arr)
  dfs(0,[])
  answer.sort()
  for(let ans of answer){
    console.log(ans)
  }
  console.log()
}