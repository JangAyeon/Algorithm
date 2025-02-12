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
        const half = Math.floor(N / 2)
        const arr = lines[1].split(" ").map(Number)
        const leftArr = arr.slice(0, half)
        const rightArr = arr.slice(half)
        let answer = 0
        const leftDic = new Map()
        // console.log(leftArr, rightArr, N, S, arr)
        leftSearch(0, 0)

        function leftSearch(sum_, index) {
            if (index == half) {
                return
            }
            const curr = leftArr[index]
            leftSearch(sum_ + curr, index + 1)
            leftSearch(sum_, index + 1)

            const value = (leftDic.get(sum_+curr)??0)+1
            leftDic.set(sum_+curr,value )
            // if (leftDicsum_ + curr]) {
            //     leftDic[sum_ + curr]++
            // } else {
            //     leftDic[sum_ + curr] = 1
            // }
            if (sum_ + curr === S) {
                answer++
            }

        }
        rightSearch(0, 0)

        function rightSearch(sum_, index) {
            if (index == N - half) {
                return
            }
            const curr = rightArr[index]
            rightSearch(sum_ + curr, index + 1)
            rightSearch(sum_, index + 1)
            const rest = S - (sum_ + curr)
            if (leftDic.has(rest)) {
                const value = leftDic.get(rest)
                answer += (value)
            }
            if (sum_ + curr === S) {
                answer++
            }

        }
        console.log(answer)

    }




)