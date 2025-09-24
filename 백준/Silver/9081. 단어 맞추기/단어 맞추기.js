const readline = require("readline")
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})


const lines = []

function solve(w){
    const arr =[...w]
    const N = arr.length
    let i = N-2
    while(i>=0 && arr[i]>=arr[i+1]){ i-- }
    if(i<0)return [false,arr.join("")]
    let j = N-1
    while(arr[i]>=arr[j]){j--}
    [arr[j], arr[i]] = [arr[i], arr[j]]
    let [left, right] = [i+1, N-1]
    while(left<right){
        [arr[left],arr[right]] = [arr[right],arr[left]]
        left+=1
        right-=1
    }

    return [true,arr.join("")]
}
rl.on("line", (line)=>lines.push(line)).on("close", ()=>{
    const T = Number(lines[0])
    const words = lines.slice(1)
    for(let w of words){
        const [flag, k] = solve(w)
        console.log(k)
        // console.log(solve(w))
    }

})
/*
4
HELLO
DRINK
SHUTTLE
ZOO
*/