function formatTime(time) {
    const [HH, MM] = time.split(":")
    return parseInt(HH) * 60 + parseInt(MM)
}

function formatPlans(plans) {
    plans = plans.map((item) => [item[0], formatTime(item[1]), parseInt(item[2])])
    return plans.sort((a, b) => a[1] - b[1])
}


function solution(plans) {
    const stack = [] // 하다가 중단된 과제
    // 과제들 시작 시간 기준으로 나열해야 함
    plans = formatPlans(plans)
    console.log(plans)
    const answer = []
    let idx;
    for(idx=0; idx<plans.length-1;idx++){
        const curr_ = plans[idx]
        const next_ = plans[idx+1]
        let mustStart = next_[1]-curr_[1]
        stack.push([curr_[0], curr_[2]])
        while(stack.length && mustStart){
            if(stack[stack.length-1][1]<=mustStart){
                const item = stack.pop() 
                answer.push(item[0])
                mustStart-=item[1]
            }
            else{
                stack[stack.length-1][1]-=mustStart
                mustStart=0
            }
            
        }
    }
    answer.push(plans[plans.length-1][0])
    while(stack.length){
        const item = stack.pop()
        answer.push(item[0])
    }

   console.log(answer)
    return answer
}

