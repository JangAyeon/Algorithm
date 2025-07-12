const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const input = [];
rl.on('line', line => input.push(line)).on('close', () => {
   // 수 갯수 N, 합 구하는 횟수 M
  	const [N,M] = input[0].split(" ").map(Number)
    const arr =  [0,...input[1].split(" ").map(Number)]
    for(let i=1;i<arr.length;i++){
        arr[i]=(arr[i-1]+arr[i])%M
    }
    arr.shift()
    // console.log(arr)
 
    const values = new Set(arr)
    const cntDic = new Map()
    for(let e of arr){
   //     console.log(e, cntDic.has(e),cntDic.get(e))
        cntDic.set(e,cntDic.has(e)?cntDic.get(e)+1:1)
    }
    const zeroCnt = cntDic.has(0)?cntDic.get(0):0
    let answer = zeroCnt
    for(let e of values){
        const v = cntDic.get(e)
        answer+= (v*(v-1))/2

    }
    console.log(answer)
    
    
});