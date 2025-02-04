const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []
rl.on("line", (line) => {

    lines.push(line.trim())


}).on("close", () => {

    const N = Number(lines[0])
    const times = lines.slice(1).map((r) => r.split(" ").map(Number))

    const schedules = []


    for (let t of times) {
        const [start, end] = t

        schedules.push({
            gap: end - start,
            start,
            end

        })

    }

    // 정렬 : 시간 순 ---> 종료 순

    schedules.sort((a, b) => {
        if (a.start === b.start) {
            return a.end - b.end
        }
        return a.start - b.start
    })



    let answer = 0
    let count = 1
    let start = -Infinity
    let end = Infinity




    for (let t of schedules) {
        const [s, e] = [t.start, t.end]
        // 갭 줄이기
        if (start < s && e < end) {

            start = s
            end = e

        } else if (end <= s) {
            count += 1
            start = s
            end = e


        }



        //console.log([s,e], count)
    }

    console.log(count)
})

/**
5
1 3
1 4
4 4
4 4
4 5


answ: 4


**/