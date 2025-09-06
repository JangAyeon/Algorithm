function solution(tickets) {
    var answer = [];
    const N = tickets.length
    const visited = Array.from({length:N}).fill(false)
    const routes = []
    function dfs(curr, route, dept){
        if(dept==N){
            answer.push(route.join(" "))
            return
        }
        for(let idx=0;idx<N;idx++){
            const next_ =  tickets[idx]
            if(visited[idx] || next_[0]!=curr)continue
            visited[idx] = true
            dfs(next_[1], [...route,next_[1]], dept+1 )
            visited[idx]=false
        }
    }
    dfs("ICN",["ICN"],0)
    answer.sort()
    return answer[0].split(" ");
}