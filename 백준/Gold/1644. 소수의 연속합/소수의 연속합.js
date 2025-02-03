const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
const lines = []
rl.on("line", (line) => {
    lines.push(line.trim())
}).on(("close"), () => {

    const N = Number(lines[0])
    const lst = new Array(N + 1).fill(true)
    lst[0] = lst[1] = false
    for (let i = 2; i < N + 1; i++) {
        for (let j = i + i; j < N + 1; j += i) {
            lst[j] = false

        }



    }
    const arr = lst.map((e, idx) => (e === true ? idx : 0)).filter((e) => e != 0)
    let start = 0
    let end = start
    let total = arr[end]
let answer = 0

    while (start<=end &&end < N + 1) {
        if (total <= N) {
            if (total == N) {
                // console.log(arr.slice(start, end + 1))
answer+=1

            }
            end += 1
total+=arr[end]

        } else {
total-=arr[start]

            start += 1
        }

    }

    console.log( answer)
})