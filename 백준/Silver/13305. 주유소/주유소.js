const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map(BigInt));
// console.log(input)

const n = input[0]
const distance = input[1]
const prices = input[2]
let minPrice = input[2][0]

let answer = BigInt(0)


for(let i=0;i<n-1;i++){
const dist = distance[i]
if(prices[i]< minPrice){
    minPrice= prices[i]
}
answer+=dist*minPrice

}
console.log(answer.toString())

