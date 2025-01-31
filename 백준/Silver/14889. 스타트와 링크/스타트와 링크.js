const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []


function makeSym(N, graph) {
    const arr = new Array(N).fill(0).map((_) => new Array(N).fill(0))
    //console.log(arr)

    for (let i = 0; i < N; i++) {

        for (let j = 0; j < N; j++) {

            arr[i][j] = arr[j][i] = graph[i][j] + graph[j][i]

        }
    }

    return arr


}


rl.on(("line"), (line) => {

    lines.push(line.trim())
}).on(("close"), () => {
    const N = Number(lines[0])
    const graph = lines.slice(1).map((e) => e.split(" ").map(Number))
    const numbers = new Array(N).fill(0).map((_, idx) => idx + 1).sort((a, b) => b - a)
    const visited = []
    const scores = makeSym(N, graph)
    let answer = (10 ** 5)


    function getScore(t1) {

        //console.log(t1)

        let score = 0
        for (let i = 0; i < t1.length; i++) {

            for (let j = i + 1; j < t1.length; j++) {
                score += scores[t1[i] - 1][t1[j] - 1]


            }
        }

        return score




    }



    function makeTimes(teams, idx) {
        if (teams.length == N/2 || idx === N) {
            if (teams.length == N/2 ) {
                const restTeam = numbers.filter((e) => !teams.includes(e))
                const t1 = restTeam.join("_")
                const t2 = teams.join("_")

                    const s1 = getScore(teams)
                    const s2 = getScore(restTeam)
                    //console.log(Math.abs(s1 - s2), t1,t2)

                    answer = Math.min(answer, Math.abs(s1 - s2))


                

            }
            return
        }

        for (let i = idx; i < N; i++) {
            teams.push(numbers[i])
            makeTimes(teams, i + 1)
            teams.pop()



        }
    }
    makeTimes([], 0)
    console.log( answer)
})


/**

4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

**/