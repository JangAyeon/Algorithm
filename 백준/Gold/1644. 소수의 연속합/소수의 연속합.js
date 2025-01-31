const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []


function getPrimes(n) {
    const numbers = new Array(n + 1).fill(true)
    numbers[0] = numbers[1] = false

    for (let i = 2; i <= n; i++) {
        for (let j = i * 2; j <= n; j += i) {
            numbers[j] = false

        }
    }

    const primes = numbers.map((e, idx) => e ? idx : 0).filter((e) => e != 0)
    // console.log("getPrimes: ", primes)
    return primes

}

function movePointers(arr, M) {
    let start = 0
    let end = 0
    let sum_ = arr[0]
    const answer = []




    while (end < arr.length) {
        const chunck = arr.slice(start, end + 1)
        const sum_ = chunck.reduce((acc, curr) => (acc += curr), 0)

        if (sum_ <= M) {
            if (sum_ == M) {
                //console.log("Match!!", arr.slice(start, end + 1))
                answer.push(chunck)

            }

            end += 1

        } else {
            start += 1

        }

    }

    return answer




}

rl.on(("line"), (line) => {
    lines.push(line.trim())
}).on(("close"), () => {
    const n = Number(lines[0])
    const primes = getPrimes(n)



    const answer = movePointers(primes, n)

    console.log(answer.length)

})