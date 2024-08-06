function formatMM(time){
    const [hh,mm]=time.split(":").map(Number)
    return hh*60+mm
}


function parseArr(plans){
    const arr = []
    for (let [a,b,c] of plans){
        arr.push([a,formatMM(b),Number(c)])
    }
    arr.sort((a,b)=>a[1]-b[1])
    return arr
}

function solution(plans) {
    plans = parseArr(plans)
    const answer = []
    const waits=[]
    let gapTime
    for(let i=0;i<plans.length-1;i++){
        const curr_ = plans[i]
        const next_ = plans[i+1]
        gapTime=next_[1]-curr_[1]
        waits.push([curr_[0], curr_[2]])
        while(waits.length && gapTime){
            
            if(waits[waits.length-1][1]-gapTime>0){
                waits[waits.length-1][1]-=gapTime
                gapTime=0
            }else{
                const item = waits.pop()
                answer.push(item[0])
                gapTime-=item[1]
            }
            
        }


    }
    answer.push(plans[plans.length-1][0])
    while(waits.length){
        answer.push(waits.pop()[0])
    }

    return answer;
}