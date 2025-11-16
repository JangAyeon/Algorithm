/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let [prev1, prev2] = [0,0]
    for(let num of nums){
       const temp =  Math.max(num+prev1, prev2)
       prev1 = prev2
       prev2 = temp
       // console.log(i,prev1, prev2)
    }
    return prev2
};