/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    const N = nums.length
    const window = new Set()
    let i = 0
    for(let j=0;j<N;j++){
        if(Math.abs(j-i)>k){
            window.delete(nums[i])
            i+=1
        }
        if(window.has(nums[j])){
            return true
        }
        window.add(nums[j])
    }
    return false

    
};