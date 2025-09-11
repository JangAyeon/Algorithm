function solution(N, costs) {
    var answer = 0;
    costs.sort((a,b)=>a[2]-b[2])
    const parents = Array.from({length:N}).fill(0).map((_,idx)=>idx)
    function find(x){
        if(parents[x]!=x){
            parents[x]=find(parents[x])
        }
        return parents[x]
    }
    function union(a,b){
        a = find(a)
        b = find(b)
        if(a!=b){
            parents[b] = parents[a]
            return true
        }
        return false
    }
    for (let cost of costs){
        const [a,b,c] = cost
        // console.log(a,b, parents[a],parents[b])
        if(union(a,b)){
            answer+=c
        }
    }
    return answer;
}