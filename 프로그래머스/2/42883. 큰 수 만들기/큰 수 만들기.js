function solution(number, k) {
    let arr = []
    for(let i of number){
        while(arr.length>0 && k>0 && arr[arr.length-1]<i){
            arr.pop()
            k-=1
        }
        arr.push(i)
    }
    const answer = arr.slice(0, arr.length - k)


    return answer.join("");
}