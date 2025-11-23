/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const numsArr = nums.map((item, idx)=> [item,idx])
    numsArr.sort((a,b) => a[0]-b[0])
    
    const N = nums.length
    let [start, end] = [0,N-1]
    while(start<end){
        const t = numsArr[start][0] + numsArr[end][0]
        console.log(t, start, end)
        if(t==target){
            return [numsArr[start][1], numsArr[end][1]]
        }
        else if(t<target){
            start++
        }else{
            end--
        }
    }
};