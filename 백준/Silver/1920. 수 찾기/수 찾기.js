const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []
rl.on("line", line => lines.push(line)).on("close", () => {


    // console.log(lines)
    const [N, M] = [+lines[0], +lines[2]]
    const arr1 = lines[1].split(" ").map(Number).sort((a, b) => a - b)
    const arr2 = lines[3].split(" ").map(Number)

    function binearySearch(target) {
        let [start, end] = [0, N - 1]
        while (start <= end) {
            const idx = parseInt((start + end) / 2)
            if (arr1[idx] > target) {
                end = idx - 1

            } else if (arr1[idx] < target) {
                start = idx + 1

            } else {
                return 1
            }

        }


        return 0
    }

    for (let e of arr2) {
        console.log(binearySearch(e))
    }
    // console.log(N, M)
    // console.log(arr1, arr2)


})