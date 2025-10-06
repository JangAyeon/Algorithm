function solution(N, results) {


    // for (c in [a ~ z])
        // A 선수 순위를 알려면
        // 나머지 선수와의 관계가 다 있어야 함
        // 플로이드 워셜
    const distance = Array.from({length:N+1},()=> Array.from({length:N+1}).fill(0))
    
    for(let [a,b] of results){
        distance[a][b]=1 // a가 b를 이김
        // distance[b][a]=1 //b가 a에게 짐
    }
    for(let i=0;i<N+1;i++){
        distance[i][i]=0
    }
    
    
    for(let c=1;c<N+1;c++){
        for(let a=1;a<N+1;a++){
            for (let b=1;b<N+1;b++){
                if((distance[a][c] && distance[c][b])){
                     distance[a][b]=1
                }
               
               
            }
        }
    }
    // console.log(distance)
    const answer = []
    for(let i=1;i<N+1;i++){
        let count = 0
        for(let j=1;j<N+1;j++){
            if(i==j)continue
            if(distance[i][j] || distance[j][i]){
                count+=1
            }
        }
        // console.log(i,count)
        if(count==N-1){
            answer.push(i)
        }
    }
    return answer.length;
}