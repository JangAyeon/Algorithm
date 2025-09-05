function solution(k, dungeons) {
    var answer = -1;
    /*
     최소 필요 피로도 <- 시작을 위함
     소모 피로도 <- 끝나면 사용되는 피로도
    */
    const n = dungeons.length
    const visited = Array.from({length:n}).fill(false)
    function dfs(dept, lst,power){
        answer = Math.max(answer, lst.length)
        if(dept==n){
            console.log(lst,power)
            
            return
        }
        for(let i=0;i<n;i++){
            if(visited[i] ||power -dungeons[i][0]<0 )continue
            visited[i]=true
            dfs(dept+1, [...lst, i],power -dungeons[i][1])
            visited[i]=false
        }
    }
    for(let start=0;start<n;start++){
        visited[start] = true
        dfs(1, [start],k-dungeons[start][1])
        visited[start]=false
    }
    
    return answer;
}