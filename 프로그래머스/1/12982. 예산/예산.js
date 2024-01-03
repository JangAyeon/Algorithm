function solution(d, budget) {
    d.sort((a,b)=>a-b)
    //console.log(d)
    let answer = 0;
    while(d.length>0 && budget>0){
        const m = d.shift()
        budget-=m
        if(budget>=0){
            answer++
            
        }
        //console.log(m)
    }
    return answer;
}