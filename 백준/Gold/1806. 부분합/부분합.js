const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []

rl.on(("line"), (line) => {
    //console.log(line.trim())
    lines.push(line.trim())

}).on(("close"), () => {
    const [N, S] = lines[0].split(" ").map(Number)
    const arr = lines[1].split(" ").map(Number)
    let start = 0
    let end = 0
    let total = arr[end]
    let answer = Infinity


    while (end < N) {
        if (total < S) {
            end += 1;
            total += arr[end]
        } else {
            //console.log(start, end, total, arr.slice(start, end + 1))
            answer = Math.min(answer, end - start + 1)


            total -= arr[start];
            start += 1
        }
    }
    console.log(answer == Infinity?0:answer)
})


/**
3 10
3 3 3
=> 0

**/

