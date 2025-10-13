function solution(land, height) {
    const directions = [[1,0],[-1,0],[0,1],[0,-1]]
    const N = land.length
    const types = Array.from({length:N}, ()=>Array.from({length:N}).fill(0))
   const visited = Array.from({length:N}, ()=>Array.from({length:N}).fill(false))

    let type=0
    const connectStack = []
    
    function bfs(i,j, type){
            // console.log("###",i,j,type)
            visited[i][j]=true
        types[i][j]=type
        const que = [[i,j]]
          while(que.length){
        const [r,c] = que.shift()
        for(let [dr, dc] of directions){
            const [nr, nc] = [r+dr, c+dc]
            if(nr<0 || nr>=N || nc<0 || nc>=N||visited[nr][nc]){continue}
            const dist = Math.abs(land[nr][nc]-land[r][c])
            // console.log([r,c],[nr, nc],dist)
            if(dist>height){
                connectStack.push([[nr,nc],[r,c],dist])
            }else{
                types[nr][nc]=type
                // types[r][c ]= type
                visited[nr][nc] = true
                que.push([nr, nc])
            }
        }
        
    
    }
    

    
}
    for(let i=0;i<N;i++){
        for(let j=0;j<N;j++){
            if(visited[i][j]){continue}
            type+=1
            bfs(i,j, type)
      
        }
    }
 // console.log(type)
const edgeMap = new Map()

for (const [[r1,c1],[r2,c2],h] of connectStack) {
  const [t1, t2] = [types[r1][c1], types[r2][c2]]
  if (t1 === t2) continue
  const key = t1 < t2 ? `${t1},${t2}` : `${t2},${t1}`
  if (!edgeMap.has(key) || edgeMap.get(key) > h) {
    edgeMap.set(key, h)
  }
}

const edges = []
for (const [key, h] of edgeMap) {
  const [a, b] = key.split(',').map(Number)
  edges.push([a, b, h])
}
    //console.log(edges)
  const parents = Array.from({length:type+1}, (_,i)=>i)
    //console.log(parents)
    
    
    edges.sort((a,b)=>a[2]-b[2])
    function findParent(a){
        if(parents[a]!=a){
            parents[a] = findParent(parents[a])         
        }
        return parents[a]
    }
    function union(a,b){
        a = findParent(a)
        b = findParent(b)
        if(a>b){
            parents[a]=b
        }else{
            parents[b]=a
        }
    }
    let answer = 0
    for(let [a,b,h] of edges){
        if(findParent(a)!=findParent(b)){
            union(a,b)
            answer+=h
            //console.log("###",a,b, distances[a][b])
        }
    }
   // console.log(parents)
    
    return answer

}