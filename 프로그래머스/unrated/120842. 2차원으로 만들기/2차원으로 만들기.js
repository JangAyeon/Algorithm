function solution(num_list, n) {
    let answer = Array.from({length:num_list.length/n},()=>[])
    for(let idx=0;idx<num_list.length;idx++){
        let index = Math.floor(idx/n)
        answer[index].push(num_list[idx])
    }
    return answer;
}