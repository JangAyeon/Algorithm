/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    const rank = nums.sort((a,b)=>-a+b)
    // console.log(rank)
    return rank[k-1]
};