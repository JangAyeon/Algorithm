//  {‘A’, ‘C’, ‘G’, ‘T’} 

//  {‘A’, ‘C’, ‘G’, ‘T’} 

const readline = require("readline")
const rl = readline.createInterface({

    input: process.stdin,
    output: process.stdout
})

function isValidPart(countDic, rulesDic){
    const keys = Object.keys(rulesDic)
    for(let k of keys){
        if(countDic.get(k)<rulesDic[k]){return false}
    }
    return true
}

const input = []
rl.on("line", line => input.push(line)).on("close", () => {
    const [N, M] = input[0].split(" ").map(Number)
    const arr = input[1].split("")
    const [A, C, G, T] = input[2].split(" ").map(Number)
    const rulesDic= {A,C,G,T}
    const countDic = new Map(Object.keys(rulesDic).map(k=>[k,0]))
    let answer = 0
    // 초기 윈도우
    for(let i=0;i<M;i++){
        countDic.set(arr[i], (countDic.get(arr[i])||0)+1)
    }
    if(isValidPart(countDic, rulesDic)) answer++
    for(let i=M;i<N;i++){
        const removed = arr[i-M]
        const added = arr[i]
        countDic.set(removed, (countDic.get(removed)||0)-1)
        countDic.set(added, (countDic.get(added)||0)+1)
        if(isValidPart(countDic, rulesDic))answer++
    }
    // console.log(N, M, arr, A, C, G, T, answer)
    console.log(answer)
})