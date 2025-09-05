function solution(answers) {
    const picks = [[1, 2, 3, 4, 5],
                   [2, 1, 2, 3, 2, 4, 2, 5],
                   [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
                 ]
    const P = picks.length
    let scores = [0,0,0]
    for(let idx = 0;idx<P;idx++){
        const pick = picks[idx]
        for(let i=0;i<answers.length;i++){
            if(pick[i%pick.length] == answers[i]){
                
                scores[idx]+=1
            }
            
        }
    }
    const max_score = Math.max(...scores)
   
    const answer = []
    for (let idx = 0;idx<scores.length;idx++){
        if(scores[idx]==max_score){
            answer.push(idx+1)
        }
        
    }
    return answer;
}