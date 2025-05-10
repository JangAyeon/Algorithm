const readline = require("readline")
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})


// 곡 갯수(N), 시작볼룸(S),  M보다 큰 값으로 볼륨 변경 불가능(M)
const lines = []
let answer = -1
rl.on("line",(input)=>{
    // console.log(input)
    lines.push(input.split(" ").map(Number))
}).on("close",()=>{
    const [N,S,M] = lines[0]
    const V = lines[1]
    // console.log(N,S,M, V)

    const dp = Array.from({length:N+1}, ()=> Array(M+1).fill(false))
    dp[0][S] = true
    for(let i=0;i<N;i++){
        for(let v=0;v<=M;v++){
            if(!dp[i][v])continue
            const [up, down] = [v+V[i],v-V[i]]
            if(up<=M){dp[i+1][up]=true}
            if(0<=down){dp[i+1][down]=true}
        }
    }
    for (let v = M;v >= 0; v--) {
        if(!dp[N][v])continue
        answer = v
        break

    }
    console.log(answer)

})