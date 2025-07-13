const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function isValidPart(countDic,rulesDic){
    for(let k of Object.keys(rulesDic)){
        // console.log(k, countDic.get(k),rulesDic[k])
        if(countDic.get(k)<rulesDic[k]){
            return false
        }
    }
    return true
}

const input = []
rl.on("line", line => input.push(line)).on("close", () => {
    const [N,M] = input[0].split(" ").map(Number)
    const arr = input[1].split("")
    let answer = 0
    // {‘A’, ‘C’, ‘G’, ‘T’} 
    const [A,C,G,T] = input[2].split(" ").map(Number)
    const rulesDic = {A, G, C, T}
    const countDic = new Map()
    for (let e of Object.keys(rulesDic)){
         countDic.set(e, 0)
    }
   
    let [start, end]=[0, M-1]
    for(let idx=0;idx<M;idx++){
        const c = arr[idx]
        const v = countDic.get(c)
        countDic.set(c, v?v+1:1)
    }
    isValidPart(countDic, rulesDic) && answer++
       // console.log(answer,countDic, rulesDic)
    while(end+1<N){
        const removed = arr[start]
        const added = arr[end+1]
        countDic.set(removed, countDic.get(removed)-1)
        countDic.set(added, (countDic.get(added)??1)+1)
        isValidPart(countDic, rulesDic) && answer++
        // console.log(answer, arr.slice(start, end+1), countDic)
        start++
        end++
    }
    

    console.log(answer)
})

// """
// 4 2
// AAAA
// 0 0 0 0
// ans: 3
// """