// 3 16

const readline = require("readline")
const rl = readline.createInterface({

    input: process.stdin,
    output: process.stdout

})


const lines = []
rl.on("line", line => lines.push(line)).on("close", () => {

    const [n, m] = lines[0].split(" ").map(Number)
    // console.log(n, m)
  	const arr = Array.from({length:m+1}).fill(false)
    arr[0]=true
    arr[1]=true
    for(let idx=2;idx<parseInt((m)**(1/2))+1;idx++){
        let step = 2
        while(idx*step<arr.length){
                   if(!arr[step*idx]){arr[step*idx]=true}
        step++ 
        }

    }
      const answer =  []
    for(let idx=0;idx<arr.length;idx++){
        !arr[idx]&& idx>=n && idx<=m && answer.push(idx)
    }
  
    console.log(answer.join("\n"))
    // console.log(arr, arr.length)


})