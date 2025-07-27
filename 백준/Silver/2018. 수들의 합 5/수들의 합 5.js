const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const input = []
rl.on("line", line => input.push(line)).on("close", () => {

    const N = +input[0]
    // const arr = Array.from({length:N}).map((_,idx)=>idx+1)
    let [start, end,sum, count] = [1,1,1,0]
    while(end<=N){
        // console.log(start, end,sum)
        if(sum<N){
            end++
            sum+=end
        }
        else if(sum>N){
            sum-=start
            start++
            
        }
        else{
            count++
            end++
            sum+=end
            
        }
    }
    console.log(count)
})