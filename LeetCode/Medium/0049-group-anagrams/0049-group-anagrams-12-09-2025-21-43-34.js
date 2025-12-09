/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const dict = {}
    for(let e of strs){
        const key = [...e].sort()
        if(dict[key]){
            dict[key].push(e)
        }else{
            dict[key] = [e]
        }
    }
    const answer = Object.values(dict)
    // function isAnagrams(s1, s2){
    //     const diff = new Set([...s1].filter((i) =>![...s2].has(i)))
    //     console.log(s1, s2, diff)
    //     return !diff.size
    // }
    // console.log(answer)
    return answer
};