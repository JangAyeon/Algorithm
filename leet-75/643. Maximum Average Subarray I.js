/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */


function getSum(arr){
    const sum_= arr.reduce((acc,curr)=>(acc+=curr),0)
    return sum_
 }
var findMaxAverage = function(nums, k) {
    let sum =  getSum(nums.slice(0, k)) 
    let maxSum =sum

    
    for(let i = 0;i+k<nums.length;i++){
        const removed = nums[i]
        const added = nums[i+k]
        sum = sum+ -removed+added
        maxSum = Math.max(maxSum, sum)
        //console.log(removed, added,maxSum)
    }
    //console.log(maxSum)
    return maxSum/k
    
};