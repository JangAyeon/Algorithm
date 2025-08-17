const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


const lines = []
rl.on("line", line => lines.push(line)).on("close", () => {
    const arr = lines[0].split("-")
    const arr1 = []

    for(let e of arr){
        const temp = e.split("+").map(Number)
        const total = temp.reduce((acc, curr)=>(acc+=curr),0)
        arr1.push(total)

    }
    let answer = arr1.shift()
    for(let e of arr1){

        answer-=e
    }


    console.log( answer)
})