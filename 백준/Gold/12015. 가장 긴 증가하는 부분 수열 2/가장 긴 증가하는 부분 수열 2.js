const readline = require("readline")
const rl = readline.createInterface({

    input: process.stdin,
    output: process.stdout


})

const lines = []


rl.on("line", (line) => {
    const s = line.trim()
    lines.push(s)
}).on("close", () => {
    const n = Number(lines[0])
    const arr = lines[1].split(" ").map(Number)
    const answer = [arr[0]]

    for(let i=1;i<n;i++){
        if(answer[answer.length-1]<arr[i]){
            answer.push(arr[i])
        }
        else{
            const idx =  binarySearch(answer, arr[i])
            answer[idx] = arr[i]
        }
    }
    // console.log(answer)



    function binarySearch(arr, target){
        let start = 0
        let end = arr.length-1
        while(start<=end){
            let mid = parseInt((start+end)/2)
            if(target>arr[mid]){start=mid+1}
            else{end=mid-1}
        }
        return start
    }
    console.log(answer.length)
})