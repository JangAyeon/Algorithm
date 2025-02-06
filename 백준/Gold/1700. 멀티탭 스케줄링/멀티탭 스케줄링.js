const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []

rl.on(("line"), (line) => {
    lines.push(line.trim())


}).on(("close"), () => {
    const [n, m] = lines[0].split(" ").map(Number)
    const arr = lines[1].split(" ").map(Number)

    let power = new Set() // 현재 멀티탭에 꽂혀있는 전기 용품
    let answer = 0

    for (let i = 0; i < m; i++) {

        const curr = arr[i]
        if (power.has(curr)) {
            continue
        }
        if (power.size < n) {
            power.add(curr)
        } else {
            let idx = new Map()
            for (let item of power) {
                let found = false
                for (let j = i + 1; j < m; j++) {

                    if (arr[j] == item) {

                        idx.set(item, j)
                        found = true
                        break
                    }
                }
                if (!found) idx.set(item,Infinity); // 이후에 안 나오면 k+1 처리
            }
            let target = [...idx.entries()].sort((a, b) => b[1] - a[1])[0][0];
            power.delete(target);
            power.add(curr);
            answer++;
        }
    }

    console.log( answer)
})