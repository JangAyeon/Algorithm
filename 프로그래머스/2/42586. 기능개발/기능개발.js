function solution(progresses, speeds) {
    const works = []
    const N = speeds.length
    for(let i=0;i<N;i++){
        works.push(Math.ceil((100-progresses[i])/speeds[i]))
    }
    // console.log(works)
    let stack = [0]
    const answer = []
    let max_work = works[0]
    for(let i=1;i<N;i++){
        // console.log(stack)
        if(stack.length && max_work<works[i]){
            max_work = works[i]
           answer.push(stack.length)
            stack = []
        }
        stack.push(i)
        
    }
    if(stack.length){
        answer.push(stack.length)
    }
    
    return answer;
}