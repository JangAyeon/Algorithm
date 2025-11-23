/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const answer = []
    const N = nums.length
    nums.sort((a,b)=>a-b)
    console.log(nums)
    let i=0
    while(i+2<N){
        
        console.log(i, nums[i])
        let [start,end] = [i+1, N-1]
        const target =  0-nums[i]
        while(start<end){
            const t = nums[start]+nums[end]
            if(t==target){
                console.log(i, start, end,[nums[i], nums[start], nums[end]] )
                answer.push([nums[i], nums[start], nums[end]])
                start++
                while(start<end && nums[start]==nums[start-1]){start++}
            }
            else if(t<target){
                start++
            }
            else{
                end--
            }
        }
        while(nums[i]==nums[i+1]){i++}
        i++
    }
    // console.log(answer)
    return answer
};