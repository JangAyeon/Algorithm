
function find_parents(node, parents){
    if(node!=parents[node]){
        node = find_parents(parents[node],parents)
    }
    return parents[node]
}

function union(a,b, parents){
    a = find_parents(a, parents)
     b = find_parents(b, parents)
    if(a<b){
        parents[b] =a
    }
    else{
        parents[a] =b
    }
}


function solution(n, costs) {
    var answer = 0;
    costs.sort((a,b)=>+a[2]-b[2])
    const parents = Array.from({length:n+1},(_,i)=>i)

    for(let cost of costs){
        if(find_parents(cost[0],parents)!=find_parents(cost[1], parents)){
            union(cost[0],cost[1],parents)
            answer+=cost[2]
        }
    }
    return answer;
}