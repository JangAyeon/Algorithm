const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []

rl.on(("line"), (line) => {

    lines.push(line.trim())


}).on(("close"), () => {
    const [N, M] = lines[0].split(" ").map(Number)
    const arr = lines[1].split(" ").map(Number)
    let start = 0
    let end = 0
    let total = arr[0]
    let answer = 0

    while (end < N) {
        // console.log(arr.slice(start, end), total, "|", start, end)


        if (total <= M) {
            if (total === M) {
                //console.log(arr.slice(start, end + 1))
                answer += 1

            }

            end += 1
            total += arr[end]
        } else {
            total -= arr[start]
            start += 1

        }
    }
    console.log(answer)
})