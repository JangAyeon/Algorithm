const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const input = []
rl.on("line", line => input.push(line)).on("close", () => {

    const N = +input[0]
    const arr = input[1].split(" ").map(Number).sort((a, b) => a - b)
    let answer= 0 
    function twoPointer(target, index) {
        let [start, end] = [0, arr.length - 1]
        while (start < end) {
            const sum = arr[start] + arr[end]
            if (sum === target) {
                if (start != index && end != index) {
                    return true
                } else if (start == index) {
                    start++
                } else {
                    end--
                }
            } else if (sum < target) {
                start++
            } else {
                end--
            }

        }
        return false

    }

    for (let index = 0; index < arr.length ; index++) {
        // console.log(arr[index], twoPointer(arr[index], index))
        twoPointer(arr[index], index) && answer++
    }
    console.log(answer)

})