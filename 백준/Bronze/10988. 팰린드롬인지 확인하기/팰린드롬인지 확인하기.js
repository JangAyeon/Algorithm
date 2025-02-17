const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdinout

})

const lines = []

rl.on("line", (line) => {
    lines.push(line.trim())
}).on("close", () => {
    const arr = lines[0].split("")
    let start = 0
    let end = arr.length - 1
    let flag = true
    while (start <= end) {
        if (arr[start] != arr[end]) {
            flag = false
            break
        }
        start += 1
        end -= 1
    }
    const answer = flag ? 1 : 0
    console.log(answer)
})