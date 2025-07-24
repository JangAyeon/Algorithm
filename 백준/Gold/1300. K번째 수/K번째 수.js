const readline = require("readline")
const rl = readline.createInterface({

    input: process.stdin,
    output: process.stdout
})

const input = []
rl.on("line", line => input.push(line)).on("close", () => {
    // console.log(input)

    const N = +input[0]
    const M = +input[1]

    function getLowerCount(num) {

        let k = 0
        for (let i = 0; i < N; i++) {
            let minCount = parseInt(num / (i + 1))
            k += Math.min(minCount, N)

        }
        return k
    }
    let start = 1
    let end = M
    let answer = 0
    while(start<=end){
        let target =parseInt( (start+end)/2)
        let count = getLowerCount(target)
        // console.log(target, count)
        if(count<M){start = target+1}
        else{
            answer =target
            end = target-1
        }
    }
    console.log(answer)
    
    









})