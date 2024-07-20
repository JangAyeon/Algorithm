
function getScore(answers, player){
    let score = 0
    for (let i=0;i<answers.length;i++){
        if (answers[i]==player[i]){
            score+=1
        }
    }
    return score
}

function solution(answers) {
    const p1 =[1, 2, 3, 4, 5]
    const p2 =[2, 1, 2, 3, 2, 4, 2, 5 ]
    const p3 =[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    const players = [p1,p2,p3]
    let maxScore = 0
    const scores = []
    
    for(let i=0;i<players.length;i++){
        const p = players[i]
        let n = (Math.ceil(answers.length/p.length))
        let player = []
        while (n){
            player = [...player, ...p]
            n-=1
        }
        const score = getScore(answers, player)
        scores.push(score)
        maxScore = Math.max(maxScore,score)
        //console.log(maxScore,scores)
    }
    const answer = []
    for (let i=0;i<scores.length;i++){
        if (scores[i]==maxScore){
            answer.push(i+1)
        }
    }

    return answer;
}