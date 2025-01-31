const readline = require("readline")
const rl = readline.createInterface({

    input: process.stdin,
    output: process.stdout

})

const lines = []

rl.on(("line"), (line) => {
    lines.push(line.trim())
}).on(("close"), () => {
    const N = Number(lines[0])
    const arr = lines.slice(1).map((e) => e.split(" ").map(Number)).flat()
    const stack = []
    for(let e of arr){
        if(e===0){
            stack.pop()
        }else{
            stack.push(e)
        }
    }
    // console.log("close", N, arr, stack)
    const sum_ = stack.reduce((acc, curr)=>(acc+=curr),0)
    console.log(sum_)
})