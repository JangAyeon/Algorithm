function getMapInfo(maps,N,M){
    const info={}
        for(let i=0;i<N;i++){
        for(let j=0;j<M;j++){
            if(maps[i][j]=="L"){
                info["L"] = [i,j]
            }else if(maps[i][j]==="E"){
                info["E"] = [i,j]
            }else if(maps[i][j]=="S"){
                info["S"] = [i,j]
            }
        }
    }
    return info
}

function solution(maps) {
    const [N,M] = [maps.length, maps[0].length]
    const info = getMapInfo(maps,N,M)
    const directions = [
        [-1,0],[1,0],[0,-1],[0,1]
    ]



    console.log(info)
    
    function bfs(start, destination){
            const que = [start]
                const visited = Array.from({length:N},()=>Array.from({length:M}).fill(-1))
    visited[start[0]][start[1]]=0
    while(que.length){
        const [r,c] = que.shift()
        if(r==destination[0] && c==destination[1]){
            // console.log(visited[r][c])
            return visited[r][c]
        }
        for(let [dr, dc] of directions){
            const [nr, nc] = [r+dr,c+dc]
            if(nr<0 || nr>=N || nc<0 || nc>=M||visited[nr][nc]!=-1 || maps[nr][nc]=="X"){
                continue
            }
            que.push([nr, nc])
            visited[nr][nc] = visited[r][c]+1
        }
    }
        return -1
    }

    const a=bfs(info.S, info.L)
    const b = bfs(info.L, info.E)
    console.log(a,b)
    if(a==-1|| b==-1){return -1}
    else{return a+b}
    


}