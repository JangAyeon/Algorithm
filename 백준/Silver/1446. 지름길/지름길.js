const readline = require("readline")
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

const lines = []
rl.on("line", line=>lines.push(line)).on("close",()=>{
    const [N,M] = lines[0].split(" ").map(Number)
    const routes = lines.slice(1).map(item=>item.split(" ").map(Number))
    const arr = Array.from({length:M+1}).fill(0).map((_,idx)=>idx) // 지름길 하나도 안 씀

    for(let i=0;i<=M;i++){
        if(i>0){arr[i] = Math.min(arr[i], arr[i-1]+1)}
        
        for(let j=0;j<N;j++){
            const [s,e,p] =routes[j]
            if(i==s&&e<=M){
                // console.log(i,e,"###",arr[s]+p, arr[e])
                arr[e]=Math.min(arr[s]+p, arr[e])
            }
        }
    }



    console.log(arr[M])
})