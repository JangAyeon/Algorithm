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
    const arr = lines.slice(1)[0].split(" ").map(Number)
    const stack = []
    const answer = new Array(N).fill(0)
    for(let i=0;i<arr.length;i++){
        
        while(stack.length>0 && arr[stack[stack.length-1]]<arr[i]){

            stack.pop()
        }
        if(stack.length>0){
            answer[i]=stack[stack.length-1]+1
        }
        stack.push(i)
    }
    console.log(answer.join(" "))
})