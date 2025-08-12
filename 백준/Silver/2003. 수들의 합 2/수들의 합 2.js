const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout

})

/*

4 2
1 1 1 1
*/

const inputs = []
rl.on("line", line => inputs.push(line)).on("close", () => {
    const [N, M] = inputs[0].split(" ").map(Number)
    const arr = inputs[1].split(" ").map(Number)
    let [start, end, total] = [0, 0, arr[0]]
    let count = 0
    //   console.log(N,M, arr)
    // console.log(start, end, total)

    while (end < N) {
        // console.log(start, end, total, count)
        if (total <= M) {
            if (total == M) {
                count++
            }
            end += 1
            total += arr[end]

        } else {
            total -= arr[start]
            start += 1
            
        }

    }
    console.log(count)
})