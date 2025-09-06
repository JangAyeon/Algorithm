function solution(N, computers) {
    var answer = 0;
    const visited = Array.from({length:N}).fill(false)
    function dfs(idx){
        for(let next_=0;next_<computers[idx].length;next_++){
            if(idx===next_)continue
            if(visited[next_] ||computers[idx][next_]===0 )continue             
            visited[next_]=true
            dfs(next_)
        }
    }
    for(let start = 0;start<N;start++){
        if(visited[start])continue
        answer++
        console.log(start)
        visited[start]=true
        dfs(start)
    }
    return answer;
}