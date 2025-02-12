const readline = require("readline")
const rl = readline.createInterface({

    input: process.stdin,
    output: process.stdout

})


const lines = []


rl.on("line", (line) => {
    lines.push(line.trim())

}).on("close", () => {
    const [N, S] = lines[0].split(" ").map(Number)
    const arr = lines[1].split(" ").map(Number)
    const half = Math.floor(N / 2)
    const leftArr = arr.slice(0, half)
    const rightArr = arr.slice(half)
    const leftDic = new Map()
    let answer = 0

    leftSearch(0, 0)

    function leftSearch(sum_, index) {
        if (index === half) {
            return
        }
        const curr = leftArr[index]
        leftSearch(sum_ + curr, index + 1)
        leftSearch(sum_, index + 1)
        const k = sum_ + curr
        const v = (leftDic.get(k) ?? 0) + 1
        leftDic.set(k, v)
        if (k === S) {
            answer++
        }
    }

    rightSearch(0, 0)

    function rightSearch(sum_, index) {
        if (index === (N - half)) {
            return
        }
        const curr = rightArr[index]
        rightSearch(sum_ + curr, index + 1)
        rightSearch(sum_, index + 1)
        const k = S - (sum_ + curr)
        if (leftDic.has(k)) {
            const v = leftDic.get(k)
            answer += v
        }
        if (k === 0) {
            
            answer++
        }
    }


    console.log( answer)
})