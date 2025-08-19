const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []
rl.on("line", line=>lines.push(line)).on("close",()=>{

const N = +lines[0]
const arr = lines.slice(1).map(Number)
const plus = []
const minus = []
const zero = []
const stack = []
for(let e of arr){
    if(e>0){
        plus.push(e)
    }
    else if(e==0){
        zero.push(e)
    }
    else{
        minus.push(e)
    }
}

minus.sort((a,b)=>a-b)
plus.sort((a,b)=>b-a)
// console.log(minus, plus, zero)
function getAcc(lst){
    while(lst.length>=2){
        const n1= lst.shift()
        const n2 = lst.shift()
        stack.push(Math.max(n1*n2, n1+n2))
    }
}
getAcc(minus)
getAcc(plus)
const rest = [...minus,...zero, ...plus]
getAcc(rest)

const answer = [...rest, ...stack].reduce((acc, curr)=>(acc+=curr),0)
// console.log(minus, plus,stack, rest)
console.log(answer)

})