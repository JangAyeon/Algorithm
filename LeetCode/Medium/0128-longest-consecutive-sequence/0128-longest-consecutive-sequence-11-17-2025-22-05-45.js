/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const numsSet = new Set(nums)
    let answer = 0
    for (let  num of numsSet){
        let length = 1
        if(!numsSet.has(num-1)){
            while(numsSet.has(num+1)){
                length+=1
                num++
            }
        }
        console.log(num, length)
        answer = Math.max(answer, length)
    }
    return answer
};