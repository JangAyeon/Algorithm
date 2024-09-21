const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim(" ")


const S = Number(input)


let total = 0
let i=1
for(;total<S;i++){
    total+=i
    if(total+(i+1)>S){
        break
    }


    
}

console.log(i)