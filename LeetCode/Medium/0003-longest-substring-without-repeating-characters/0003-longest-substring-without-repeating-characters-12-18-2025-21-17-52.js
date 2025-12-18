/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(str) {
    let [s,e] = [0,0]
    const N = str.length
    const counter = new Map()
    // let answer = new Set()
    let maxLength = 0
    
    while(s<=e && e<N){
        const val1 = (counter.get(str[e])||0)+1
        counter.set(str[e], val1)
        // console.log(s,str[e], counter.get(str[e]))
        
        while( s<=e && counter.get(str[e])>1){
            const val2 = (counter.get(str[s])||0)-1
            counter.set(str[s], val2)
            s++

        }
        const substring = str.slice(s,e+1)
        maxLength = Math.max(substring.length, maxLength)
        // if(substring.length>maxLength){
        //     // answer = new Set([substring])
        //     maxLength = substring.length
        // }
        // else if(substring.length == maxLength){
        //     answer.add(substring)
        // }
        // console.log(str.slice(s,e+1),counter)
        e++
    }
    // console.log(maxLength)
    return maxLength
    
};