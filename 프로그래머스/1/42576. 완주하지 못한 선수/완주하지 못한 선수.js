function solution(participant, completion) {
    let answer = ""
    const cp = new Map()
    for (let p of participant){
        cp.set(p,(cp.get(p)||0)+1)
    }
    const cc = new Map()
    for(let c of completion){
        cc.set(c,(cc.get(c)||0)+1)
        
    }
    
    for (let [k,v] of cp.entries()){
        if((cp.get(k)-cc.get(k))!=0){
            answer = k
            break
        }
    }

    // console.log(cp, cc)
    return answer;
}