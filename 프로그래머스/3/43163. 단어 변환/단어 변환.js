function solution(begin, target, words) {
    var answer = [];
    const N = words.length
    const visited = Array.from({length:N}).fill(false)
    function getDiffCount(str1, str2){
        const M = str1.length
        let count = 0
        for(let idx=0;idx<M;idx++){
            if(str1[idx]!=str2[idx]){count++}
        }
        // console.log("## diff", str1, str2, count)
        return count
    }
    function dfs(dept, curr, lst){
        if(curr===target){
            // console.log(dept, lst)
            answer.push(dept)
        }
        for(let idx=0;idx<N;idx++){
            if(visited[idx]||getDiffCount(curr, words[idx])>1)continue
            visited[idx]=true
            dfs(dept+1, words[idx], [...lst, words[idx]])
            visited[idx]=false
            
        }
        
    }
    dfs(0, begin, [begin])
    // console.log("###", answer)
    return answer.length>0?Math.min(...answer):0;
}