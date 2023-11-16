let fs = require("fs")
let input = fs.readFileSync("../input.txt").toString().split("\n")

let n = Number(input[0])
let arr = input[1].split(" ").map(Number)
arr.sort((x,y)=>y-x)
let k = Number(input[2])
// start는 최소값이 아니라 1이어여함
// => start가 최소값이면... 모든 건물이 같은 높이인 경우 답이 안 나옴 
let start = 1
let end = arr[0]

// console.log(n,arr,k)
let answer=-1
while(start<=end){

  let mid = Math.floor((start+end)/2)
  let total=0;

  for(let money of arr){
    total+=Math.min(mid, money)
  }

  if(total<=k){
    start = mid+1
    answer=Math.max(answer, mid)
  }
  else{
    end=mid-1
  }
}


console.log(answer)