const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().split("\n")
const N = Number(input[0])
let answer = 0

// 5로 최대한 빼고
let n = parseInt(N/5)
let flag = false
let cnt5;
let cnt3;

for(cnt5=n;cnt5>=0;cnt5--){
    cnt3 = parseInt((N-5*cnt5)/3)
    if(cnt5*5+cnt3*3==N){
        flag=true
        break
    }
    
}
if(flag){
    console.log(cnt5+cnt3)
}else{
    console.log(-1)
}