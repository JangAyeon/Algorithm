const readline = require("readline")
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

const lines=[]

function gcd(a,b){
    while(b!=0){
        const r = a%b
        a=b
        b=r
    }
    return a
}
rl.on("line", line=>lines.push(line)).on("close", ()=>{
    
    const [M,N] = lines[0].split(" ").map(BigInt)
    const k = gcd(M,N)
    
    const answer = Array.from({length:Number(k)}).fill(1).join("")
    
    console.log( answer)
})