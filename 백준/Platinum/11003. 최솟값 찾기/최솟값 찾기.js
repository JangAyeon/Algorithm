const input = require("fs").readFileSync("/dev/stdin").toString().trim().split('\n')

function solve(input) {
    const [N, L] = input[0].split(" ").map(Number)
    const arr = input[1].split(" ").map(Number)
    let [left,right]=[0, 1]
    const deque = Array(N)
    deque[0] = [arr[0],0] // value, index
    let result = arr[0]+" "

    for(let i =1 ;i<N;i++){
        if(i%1000==0){
            process.stdout.write(result)
            result = ""
        }
        // console.log(left, right, deque[left], deque[right-1])
        while(right>left && deque[left][1]<=i-L){left++}
        while(right>left && deque[right-1][0]>=arr[i]){right--}
        deque[right++]=[arr[i],i]
        result += deque[left][0]+" "
    }
    process.stdout.write(result)
    // console.log(N, L, arr)
}



solve(input)