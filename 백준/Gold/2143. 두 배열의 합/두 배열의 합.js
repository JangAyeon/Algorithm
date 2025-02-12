const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []


rl.on("line", (line) => {
    lines.push(line.trim())
}).on("close", () => {
    const N = Number(lines[0])
    const K = Number(lines[1])
    const arr1 = lines[2].split(" ").map(Number)
    const P = Number(lines[3])
    const arr2 = lines[4].split(" ").map(Number)
    const arr1Dic = new Map()
    let answer = 0
    // 구간 합 arr1
    for (let i = 0; i < K; i++) {
        let pre_sum = 0
        for (let j = i; j < K; j++) {
            pre_sum += arr1[j]
            const v = (arr1Dic.get(pre_sum) ?? 0) + 1
            arr1Dic.set(pre_sum, v)
        }
    }


    // 구간 합 arr2
        for (let i = 0; i < P; i++) {
        let pre_sum = 0
        for (let j = i; j < P; j++) {
            pre_sum += arr2[j]
            const v = (arr1Dic.get(N-pre_sum) ?? 0) 
            answer+=v
           
        }
    }
    //console.log("close", N, K, P)
    //console.log("close", arr1, arr2)
    console.log(answer)
})