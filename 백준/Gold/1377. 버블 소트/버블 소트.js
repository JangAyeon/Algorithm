const readline =  require("readline")
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})


const input = []
rl.on("line", line => input.push(line)).on("close", ()=>{
    const [N, ...res] = input.map(Number)
    const originalArr = res.map((e, idx)=>[e, idx])
    const sortedArr = res.map((e, idx)=>[e, idx]).sort((a,b) =>a[0]-b[0])
    // console.log(originalArr)
    // console.log(sortedArr)
    let answer = 0
    for(let i=0;i<N;i++){
        answer = Math.max(answer, sortedArr[i][1]-i)
    }
    console.log(answer+1)


    // console.log(N, res)
})