function solution(board) {
    const [R,C] = [board.length, board[0].length]
    const visited = Array.from({length:R},()=>Array.from({length:C}).fill(0))
    const info = {}
    const directions = [
        [1,0],[-1,0],[0,1],[0,-1]
    ]
    for(let i=0;i<R;i++){
        for(let j=0;j<C;j++){
            if(board[i][j]=="R"){
                info["start"] = [i,j]
            }else if(board[i][j]=="G"){
                info["end"] = [i,j]
            }
        }
    }
    const que = [[...info["start"],0]]
    let answer = -1
    while(que.length){
        let [r,c,dist] = que.shift()
        if(r==info["end"][0] && c==info["end"][1]){
            answer = (dist)
            break
        }
        for(let [dr, dc] of directions){
            let [rr, cc] = [r,c]
            while(true){
                let [nr,nc] = [rr+dr,cc+dc]
                if(0>nr || nr>=R || 0>nc || nc>=C || board[nr][nc]=="D"){
                    break
                }
                [rr,cc ]= [nr,nc]
            }
            if(!visited[rr][cc]){
                visited[rr][cc]=true
                que.push([rr,cc,dist+1])
            }
        }
    }
    console.log(info)
    return answer;
}