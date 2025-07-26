const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const input = [];

rl.on("line", (line) => input.push(line)).on("close", () => {
    const N = +input[0]
    const M = +input[1]
    const arr = input[2].split(" ").map(Number).sort((a,b)=>a-b)
    let [start, end, answer] = [0,N-1,0]
    
    while(start<end ){
        const total = arr[start] + arr[end]
        // console.log(total, start, end, answer)
        if(total==M){
            answer+=1
            start+=1
            end-=1
        }
        else if(total<M){
            start+=1
        }else{
            end-=1
        }
    }
    // console.log(N,M, arr);
    console.log(answer)
});