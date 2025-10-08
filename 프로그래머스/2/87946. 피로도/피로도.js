function solution(k, dungeons) {
    const N = dungeons.length
    const visited = Array.from({length:N}).fill(false)
    let answer = 0
    //  ["최소 필요 피로도", "소모 피로도"] 
    function isAble(max_strength,arr){
        let strength = max_strength
        for(let idx of arr){
            const d = dungeons[idx]
            // console.log(d)
            // console.log(strength, arr)
            if(d[0]>strength){
                return false
            }
            strength -=d[1]
        }
        return true
    }
    
    function dfs(node,level, route){
        // console.log(route,isAble(k,route), level)
        if(isAble(k,route) && route.length>answer){
            answer = route.length
        }
        if(level==N){
            return
        }
        for(let i=0;i<N;i++){
            if(visited[i]){continue}
            visited[i]=true
            dfs(i, level+1, [...route,i])
            visited[i]=false
        }
    }
    
    for(let i=0;i<N;i++){
        visited[i]=true
        dfs(i, 1, [i])
        visited[i]=false
    }
    return answer;
}