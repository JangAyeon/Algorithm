const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const input = [];
rl.on('line', line => input.push(line)).on('close', () => {
   // 수 갯수 N, 합 구하는 횟수 M
  	const [N,M] = input[0].split(" ").map(Number)
    const arr = input[1].split(" ").map(Number)
    const T = input.slice(2).map(item => item.split(" ").map(Number))
    // console.log(N,M, arr, T)
    const accSum = [0]
    for(let e of arr){
        accSum.push(accSum[accSum.length-1]+e)
    }
    const answer = []
    for(let [start, end] of T){
        const res = accSum[end]-accSum[start-1]
        answer.push(res)
    }
    for(let e of answer){
        console.log(e)
    }
});