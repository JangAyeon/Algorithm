function solution(N, stages) {
    const count = new Array(N+2).fill(0)
    let total = stages.length
    const failRate= []
    for(let s of stages){
        count[s]+=1
    }
    for (let idx=1;idx<count.length-1;idx++){
        //console.log(count[idx],total)
        failRate.push([count[idx]/total,idx])
        total-=count[idx]
       
    }
 
    failRate.sort((a,b)=>(-a[0]+b[0]))
    //console.log(failRate)
    const answer = []
    for(let e of failRate){
        answer.push(e[1])
    }

    return answer;
}