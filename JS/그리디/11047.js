//https://www.acmicpc.net/problem/11004

let fs = require("fs");
let input = fs.readFileSync("../input.txt").toString().split("\n");

let [n, k] = input[0].split(" ").map((x) => Number(x));
let arr=[]
for(let i=1;i<=n;i++){
  arr.push(Number(input[i]))
}

arr.sort((x, y) => y-x);

let answer = 0;
let money = k;

for(let item of arr){
  let j = parseInt(money / item) // 몫
answer+=j
money-=item*j
}


console.log(answer);
