function solution(answers) {
    const p1 =[1, 2, 3, 4, 5]
    const p2 =[2, 1, 2, 3, 2, 4, 2, 5 ]
    const p3 =[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    const players = [p1,p2,p3]
    const n = answers.length
    const scores = new Array(3).fill(0)
    const answer = []
    for(const [i, answer] of answers.entries()){
        for(const [j, p] of players.entries()){
            if(answer == p[i % p.length]){
                scores[j]+=1
            }
        }
    }
    const maxScore = Math.max(...scores)
    // console.log(scores,maxScore)
    for(let i=0; i<scores.length;i++){
        if (scores[i]==maxScore){
            answer.push(i+1)    
        }
        
    }

    return answer;
}