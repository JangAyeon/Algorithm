/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const complement = new Map()
    const N = nums.length
    for(let i=0;i<N;i++){
        const m = target - nums[i]
        if(complement.has(m)){
            return [complement.get(m),i]
        }
        complement.set(nums[i],i)
    }

};