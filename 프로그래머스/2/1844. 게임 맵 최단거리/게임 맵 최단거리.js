function solution(maps) {
    const [N,M] = [maps.length, maps[0].length]
    var answer = -1;
    const dir = [[0,-1],[0,1],[-1,0],[1,0]]
    const que = [[N-1,M-1]]
    while(que.length>0){
        const [r,c] = que.shift()
        if(r==0 && c==0){
            answer=(maps[r][c])
            break
        }
        for(let idx=0;idx<4;idx++){
            const [nr, nc] = [r+dir[idx][0],c+dir[idx][1]]
             // console.log(nr, nc)
            
            /*범위여부*/
            if(nr>=N||nr<0 || nc<0||nc>=M ||maps[nr][nc]!=1){continue}
            
            maps[nr][nc]=maps[r][c]+1
            que.push([nr, nc])
            
        }
    }
    
  
    return answer;
}