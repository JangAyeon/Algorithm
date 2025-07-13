const readline = require("readline")
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

const input = []
rl.on("line", line =>input.push(line)).on("close", ()=>{

    // console.log(input)
    const [N,M] = input[0].split(" ").map(Number)
    const arr = [0,...input[1].split(" ").map(Number)]
    for(let idx=1;idx<N+1;idx++){
        arr[idx] = (arr[idx]+arr[idx-1])%M
    }
    // console.log(arr)
    arr.shift() // pad로 넣은 0 빼기
    const countDic = new Map()
    for(let e of arr){
        
        countDic.set(e, countDic.get(e)+1||1)
    }
    let answer = countDic.get(0)||0
    for(let e of countDic.values()){
        answer+=(e*(e-1)/2)
    }
    // console.log(N,M, arr)
    console.log( answer)
})