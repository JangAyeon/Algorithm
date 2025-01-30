const readline = require("readline")
const rl = readline.createInterface({
input:process.stdin,
output:process.stdout

})

const lines = []

rl.on(("line"),(line)=>{
lines.push(line.trim())


}).on(("close"),()=>{
const [N,M] = lines[0].split(" ").map(Number)
const arr = lines.slice(1).map((row)=>row.split(" ").map(Number))
const pre_ = new Array(N+1).fill(0).map(()=>new Array(M+1).fill(0))
let answer = -Infinity;    

for(let i=1;i<N+1;i++){
    for(let j=1;j<M+1;j++){
        pre_[i][j]=pre_[i-1][j]+pre_[i][j-1]-pre_[i-1][j-1]+arr[i-1][j-1]
    }
}

for(let i=1;i<N+1;i++){
    for(let j=1;j<M+1;j++){
        for(let r=i;r<N+1;r++){
            for(let c=j;c<M+1;c++){
                const t = pre_[r][c] - pre_[i-1][c] - pre_[r][j-1] + pre_[i-1][j-1]
                answer = Math.max(answer, t);

            }
            
        }
    }
}
console.log(answer)
})