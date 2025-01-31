const readline = require("readline")

const rl = readline.createInterface({

    input: process.stdin,
    output: process.stdout

})

const lines = []

rl.on(("line"), (line) => {
    lines.push(line.trim())
}).on(("close"), () => {
    const n = Number(lines[0])
    const arr = lines[1].split(" ").map(Number)
    const sum_ = arr.reduce((acc, curr) => (acc += curr), 0)

    const numbers = new Array(sum_ + 2).fill(false)
    numbers[0] = true
    arr.forEach((e) => numbers[e] = true)




    function dfs(idx, total, lst) {



        if (idx == n) {
            // console.log("###", total, lst)
            numbers[total] = true



            return

        }
        for (let i = idx; i < n; i++) {
            //console.log(idx,i, total, lst)

            lst.push(arr[i])
            numbers[total + arr[i]] = true
            dfs(i + 1, total + arr[i], lst)
            lst.pop()
        }


    }
    // console.log("close", arr, n)



    dfs(0, 0, [])
    // console.log(numbers)

    const answer = numbers.map((e, idx) => e == false ? idx : 0).filter((e) => e != 0)
    console.log(answer[0])
})