/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    const N = nums.length
    for(let i=0;i<N;i++){
        for(let gap=1;gap<=k && i+gap<N ;gap++){
            // console.log(nums[i], nums[i+gap])
            if(nums[i]==nums[i+gap]){return true}
        }
    }
    return false
    
};