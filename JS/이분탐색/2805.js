let fs = require("fs")
let input = fs.readFileSync("../input.txt").toString().split("\n")

let [n,m]=input[0].split(" ").map(Number)
let arr = input[1].split(" ").map(Number)

// console.log(n,m,arr)

let start=0 // 가장 총량이 많이 잘리는
let end = arr.reduce((x,y)=>Math.max(x,y)) // 가장 총량이 작게 잘리는


let answer=-1
while (start<=end){
  let mid = Math.floor((start+end)/2)
  let total=0

  for(let tree of arr){

    rest = Math.min(mid, tree)
    total+=tree-rest
  }

  if(total<m){ // 필요한 높이 충족 못함 => 더 많이 잘리게 해야함 => 자르는 높이 낮춰
    end = mid-1
  }
  else{
    start=mid+1
    answer = Math.max(answer, mid);
  }
}

console.log(answer)