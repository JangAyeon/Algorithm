function solution(n, words) {

    const arr = [words[0]]
    for(let i=1;i<words.length;i++){
        const prev = arr[arr.length-1]
        const curr = words[i]
        // console.log(prev,prev[prev.length-1],curr,curr[0])
        if(prev[prev.length-1]!=curr[0]){
            return [i%n+1,Math.floor(i/n)+1]

        }
        if(arr.includes(curr)){
            return [i%n+1,Math.floor(i/n)+1]

        }
        arr.push(curr)
    }
    



    return [0,0];
}