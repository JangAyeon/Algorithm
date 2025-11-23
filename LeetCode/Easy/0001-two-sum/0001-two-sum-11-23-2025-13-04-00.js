/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    nums = nums.map((item, idx)=> [item,idx])
    nums.sort((a,b) => a[0]-b[0])
    
    const N = nums.length
    let [start, end] = [0,N-1]
    while(start<end){
        const t = nums[start][0] + nums[end][0]
        console.log(t, start, end)
        if(t==target){
            return [nums[start][1], nums[end][1]]
        }
        else if(t<target){
            start++
        }else{
            end--
        }
    }
};