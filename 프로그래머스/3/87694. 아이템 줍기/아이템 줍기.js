function solution(rectangles, characterX, characterY, itemX, itemY) {
    [ characterX, characterY, itemX, itemY] = [ characterX*2, characterY*2, itemX*2, itemY*2]
    const N = 102
    const graph = Array.from({length:N},()=>Array.from({length:N}).fill(0))
    const visited = Array.from({length:N},()=>Array.from({length:N}).fill(-1))

    for(let [c1,r1,c2,r2] of rectangles){
        for(let r=r1*2;r<=r2*2;r++){
            for(let c=c1*2;c<=c2*2;c++){
                 graph[r][c]=1 // 영역 전체 다
            }
            
        }
    }
    for(let [c1,r1,c2,r2] of rectangles){
        for(let r=r1*2+1;r<r2*2;r++){
            for(let c=c1*2+1;c<c2*2;c++){
               
                graph[r][c]=0 // 영역 내부만
                
                 
            }
            
        }
    }
    
    const directions = [[-1,0],[1,0],[0,1],[0,-1]]
    const que = [[characterY,characterX]]
    visited[characterY][characterX] = 0
    while(que.length){
        const [r,c] = que.shift()
        if(r ===itemY && c ==itemX){
            
            return visited[r][c]/2
        }
        for(let [dr,dc] of directions){
            const [nr, nc] = [r+dr, c+dc]
            if(nr<0 || nr>=N || nc<0 || nc>=N || visited[nr][nc]!=-1 || graph[nr][nc]==0){continue}
            que.push([nr, nc])
            visited[nr][nc] = visited[r][c]+1
        }
    }
    return 0;
}