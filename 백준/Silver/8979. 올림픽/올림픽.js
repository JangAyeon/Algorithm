const readline = require("readline")
const rl = readline.createInterface({
input:process.stdin,
output:process.stdout

})

const lines = []

rl.on(("line"),(line)=>{
lines.push(line.trim())


}).on(("close"),()=>{
const [N,K] = lines[0].split(" ").map(Number)
const arr = lines.slice(1).map((row)=>row.split(" ").map(Number))
arr.sort((a,b)=>{
    if(b[1]!=a[1])return b[1]-a[1]
    else if(b[2]!=a[2]) return b[2]-a[2]
    else return b[3]-a[3]
})
const idx = arr.findIndex((e) => e[0] === K);
const score1 = arr[idx].slice(1).join("_")
let answer
for(let i=0;i<arr.length;i++){
const score2 = arr[i].slice(1).join("_")
     //console.log(score1, score2, i)
    if(score1==score2){
        answer = (i+1)
        break
    }
   
    
}
console.log( answer)
})