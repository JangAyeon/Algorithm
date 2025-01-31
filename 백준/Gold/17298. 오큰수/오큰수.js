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
    const arr = lines[1].split(" ").map(Number)
    const lst = arr.map((_, idx)=>arr[arr.length-idx-1])
    const answer = new Array(N).fill(-1)
    const stack = []

    for(let i=0;i<N;i++){
        while(stack.length>0 && stack[stack.length-1]<=lst[i]){
            stack.pop()
        }
        if(stack.length>0){
            answer[i]=stack[stack.length-1]
        }

        stack.push(lst[i])
    }
    const reversed = answer.map((_, idx)=>answer[answer.length-idx-1]).join(" ")
    console.log(reversed)
})