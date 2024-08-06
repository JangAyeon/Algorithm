function solution(players, callings) {
    const p = {}
    const order = {}
    for(let i=0;i<players.length;i++){
        p[players[i]]=i
        order[i]=players[i]
    }
    for(let name of callings){
        const prev_order = p[name]-1
        const prev_name = order[prev_order]
        order[prev_order]=name
        order[p[name]]=prev_name
        p[name]-=1
        p[prev_name]+=1
        //console.log(name)
        //console.log(order,p)
    }
    const answer = []
    for(let i=0;i<players.length;i++){
        answer.push(order[i])
    }
    //console.log(answer)

    return answer;
}