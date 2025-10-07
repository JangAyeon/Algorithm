function solution(N, results) {
    let answer = 0;
    const graph = Array.from({length:N+1},()=>Array.from({length:N+1}).fill(0))
    for(let [a,b] of results){
        graph[a][b]=1
    }
    
    for(let c=1;c<N+1;c++){
        for(let a=1;a<N+1;a++){
            for(let b=1;b<N+1;b++){
                if(graph[a][c] && graph[c][b]){graph[a][b]=1}
            }
        }
    }
    
    for(let i=1;i<N+1;i++){
        let count = 0
        for(let j=1;j<N+1;j++){
            if(i==j){continue}
            if(graph[i][j] || graph[j][i]){
                count+=1
            }
        }
        if(count==N-1){
            answer+=1
        }
    }
    return answer;
}