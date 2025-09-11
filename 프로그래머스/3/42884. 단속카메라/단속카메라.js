function solution(routes) {
    var answer = 1;
    routes.sort((a,b)=>a[0]-b[0])
    console.log(routes)
    let [start,end] = [routes[0][0],routes[0][1]]
    for(let [s,e] of routes){
        if(start<=s && s<=end ){
            start = Math.max(start, s)
            end = Math.min(end,e)      
            // console.log(start, end, s, e, answer, "**")
        }else{
            answer+=1
            start = s
            end=e
            // console.log(start, end, s, e, answer, "****")
        }
        
    }
    return answer;
}