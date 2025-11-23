/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const numsSet = new Set(nums)
    let answer = 0
    for(let i of numsSet){
        if(!numsSet.has(i-1)){
            let count = 1
            while(numsSet.has(i+1)){
                count+=1
                i +=1
            }
            // console.log(i, count)
            answer= Math.max(count, answer)
        }
    }
    return answer
};