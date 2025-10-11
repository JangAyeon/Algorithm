function solution(land) {
    const [N,M] = [land.length, land[0].length]
    const visited=Array.from({length:N},()=>Array.from({length:M}).fill(false))
    
    const directions =[
        [1,0],[-1,0],[0,1],[0,-1]
    ]
    const chuncks = Array.from({length:M}).fill(0)
    
    function bfs(i,j){
        const que = [[i,j]]
        visited[i][j]=true
        let [size, min_c, max_c] = [1,j,j]
        while(que.length){
            const [r,c] = que.shift()
            for(let [dr, dc] of directions){
                const [nr, nc] = [r+dr, c+dc]
                if(0>nr || N<=nr || 0>nc || M<=nc||land[nr][nc]==0||visited[nr][nc]){continue}
                visited[nr][nc]=true
                size+=1
                que.push([nr, nc])
                min_c = Math.min(min_c, nc)
                max_c = Math.max(max_c, nc)
                
            }
        }
        // chuncks.push({size,min_c, max_c})
        for(let c=min_c;c<=max_c;c++){
           chuncks[c]+=size 
        }
        // console.log(i,j,size, min_c, max_c)
    }
    
    for(let i=0;i<N;i++){
        for(let j=0;j<M;j++){
            if(land[i][j]==1 && !visited[i][j]){
                bfs(i,j)
            }
        }
    }
    // console.log(chuncks)
    const max_size = Math.max(...chuncks)
  
    return max_size;
}