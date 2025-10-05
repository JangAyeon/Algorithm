function solution(priorities, location) {
    var answer = [];
    let N = priorities.length
    let priority = Math.max(...priorities)
    const arr = Array.from({length:N}).fill(0).map((_,idx)=>[String.fromCharCode(65+idx), idx])

    while(arr.length>0){
        const [c, index] = arr.shift()
        const p = priorities.shift()

        if(p>=priority){
            answer.push(c)
            priority=Math.max(...priorities)
            if(index==location){
            // console.log(answer, answer.length)
            return answer.length
            }
        }
        else{
            arr.push([c, index])
            priorities.push(p)
        }
        // console.log(priorities, arr, index)
    }
    // console.log("###", answer)
}