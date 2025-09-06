function solution(numbers, target) {
    var answer = 0;
    const N= numbers.length
    function dfs(idx, total, lst){
        if(idx==N){
            // console.log(total, lst)
            if(total==target){
                answer++
            }
            return
        }
        dfs(idx+1, total+numbers[idx]*1, [...lst,numbers[idx]*1 ])
        dfs(idx+1, total+numbers[idx]*(-1), [...lst,numbers[idx]*(-1) ])
    }
    dfs(0,0,[])
    return answer;
}