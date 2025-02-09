const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


const lines = []

rl.on("line", (line) => {

    const s = line.trim()
    lines.push(s)

}).on("close", () => {
    const [N, M] = lines[0].split(" ").map(Number)
    const half = Math.floor(N / 2)
    const arr = lines[1].split(" ").map(Number)
    const leftArr = arr.slice(0, half)
    const rightArr = arr.slice(half)
    const leftDic = {}
    let answer = 0

    leftSearch(0, 0);

    function leftSearch(sum_, index) {
        if (index == half) {
            return
        }
        const curr = leftArr[index]
        leftSearch(sum_ + curr, index + 1)
        leftSearch(sum_, index + 1)
        if (leftDic[sum_ + curr]) {
            leftDic[sum_ + curr]++
        } else {
            leftDic[sum_ + curr] = 1
        }
        if (M === sum_ + curr) {
            answer++
        }
    }

    rightSearch(0, 0);

    function rightSearch(sum_, index) {
        if (index == (N - half)) {
            return
        }
        const curr = rightArr[index]
        rightSearch(sum_ + curr, index + 1)
        rightSearch(sum_, index + 1)
        const restValue = M - (sum_ + curr)
        if (leftDic[restValue]) {
            answer += leftDic[restValue]
        }
        if (sum_ + curr == M) {
            answer++
        }
    }

    console.log(answer)




})


/**
5 0
0 0 0 0 0
ans: 31
**/