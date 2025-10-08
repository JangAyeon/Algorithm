function solution(words) {
    const keys = new Set(words)
    const dictionary = new Map()
    for (let key of keys){
        dictionary.set(key, -1)
    }
    // console.log(dictionary)
    const answer = []
    for(let index =0 ;index<words.length;index++){
        const v = dictionary.get(words[index])
        const value = v==-1?-1:index-v 
        answer.push(value)
        dictionary.set(words[index], index)
        
    }
    
    // console.log(answer)
    
    return answer;
}