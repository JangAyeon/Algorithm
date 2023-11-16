// https://velog.io/@ttc1018/%EB%B0%B1%EC%A4%80-1493%EB%B0%95%EC%8A%A4%EC%B1%84%EC%9A%B0%EA%B8%B0-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

let fs = require("fs")
let input = fs.readFileSync("../input.txt").toString().split("\n")

let [l,w,h] = input[0].split(" ").map(Number)
let totalV=l*w*h
let n = Number(input[1])
arr = []
for(let j=2;j<=n+1;j++){
  // 한변 지수, 큐브 갯수
  let [a, b] = input[j].split(" ").map(Number)  
  let s = 2**a
  // 부피, 갯수, 한변
  arr.push([s*s*s,b,s])
}

arr.sort((a,b)=>b[0]-a[0])

answer = 0
total_now = 0
for(let box of arr){
  // 다음 순서 = 이전 정육면체 부피의 1/8이므로 이전까지의 개수에 8을 곱해줌 (예 : 4*4*4 1개 = 2*2*2 8개)
  total_now *=8
  
  // 현재 공간에 채울 수 있는 갯수 -  지금까지 채운 갯수
 let cnt_limit = Math.floor(l / box[2])* Math.floor(h / box[2])* Math.floor(w / box[2])-total_now;
cnt_limit = Math.min(box[1], cnt_limit)

answer+=cnt_limit
total_now+=cnt_limit
  



}
if (total_now !=totalV) {
  console.log(-1);
} else {
  console.log(answer);
}

