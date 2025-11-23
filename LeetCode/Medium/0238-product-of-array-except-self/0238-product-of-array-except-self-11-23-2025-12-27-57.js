/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const N = nums.length
    const result = Array.from({length:N}).fill(1)
    let pointer = nums[0]
    for(let i=1;i<N;i++){
        result[i] = pointer
        pointer *=nums[i]
    }
    pointer = 1
    for(let i=N-1;i>-1;i--){
        result[i]*=pointer
        pointer*=nums[i]
    }
    // console.log(result)
    return result
};