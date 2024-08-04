const d=[[0,1],[0,-1],[1,0],[-1,0]]



function isAble(nr, nc, ROW, COL){
    if (!(0<=nr && nr<ROW)){
        return false
    }
    else if (!(0<=nc && nc<COL)){
        return false
    }
    return true
}

function bfs(start, end,maps,ROW, COL){
    const visited = [...new Array(ROW)].map((_,i)=>new Array(COL).fill(0))
    const que = [start]
    
    while (que.length){
        const [r,c] = que.shift()
        if ((r===end[0] && c==end[1])){
            //console.log("end",visited[r][c])
            return visited[r][c]
        }
        for(let [dr, dc] of d){
            const [nr, nc] = [r+dr,c+dc]
            // 범위에 벗어남 && 이미 방문함 && 갈 수 있는 곳이 아님
 
            if (!(isAble(nr, nc, ROW, COL)) || visited[nr][nc]!=0 || maps[nr][nc]=="X"){
                continue
            }
            visited[nr][nc]=visited[r][c]+1
            que.push([nr, nc])


            //console.log("###",nr,nc)
  
            
        }
        
    }
    return 0
}

function solution(maps) {
    
    const arr = []
    const [ROW, COL] = [maps.length, maps[0].length]
    
    const location={}
    const loc = ["S", "L","E"]

    const visited = [...new Array(ROW)].map((_,i)=>new Array(COL).fill(0))

    //console.log(visited)
    // 시작, 도착, 레버
    for(let idx=0;idx<maps.length;idx++){
        arr.push(maps[idx].split())
        for(let l of loc){
            if(maps[idx].includes(l)){
                location[l]=[idx, maps[idx].indexOf(l)]
            }
        }
    }
    const distance = [bfs(location["S"], location["L"],maps, ROW, COL), bfs(location["L"], location["E"],maps, ROW, COL)]
    
    
    
    
    
    if (distance.includes(0)){
        return -1
    }
    else{
        const answer = distance.reduce((num, prev)=>(num+prev),0)
        return answer
    }

}