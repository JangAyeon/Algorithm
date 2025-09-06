function solution(word) {
    var answer = 0;
    const arr = ['A', 'E', 'I', 'O', 'U']
    const N = arr.length
    let isFind = false
    function dfs(idx, lst){
        // console.log(lst.join(""),answer)
        if(isFind){return}
        answer++
        if(lst.join("") === word){
            console.log("####",lst, --answer)
            isFind=true
            return
        }
        if(lst.length == N){
            return
        }
        for(let idx=0;idx<N;idx++){
            dfs(idx+1, [...lst, arr[idx]])
        }
    }
    dfs(0,[])
    return answer;
}