/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const N = nums.length
    const answer = []
    nums.sort((a,b)=>a-b)
    for(let i=0;i<N;i++){
        const target = 0-nums[i]
        let [start, end] = [i+1, N-1]
        if(i>0 && nums[i]==nums[i-1]){continue}
        while(start<end){
            const t = nums[start]+nums[end]
           // console.log(start, end, t, target)
            if(t>target){end-=1}
            else{
                if(t==target){
                    answer.push( [nums[i], nums[start],nums[end]])
                    //console.log("##",i, start, end)
                }
                while(start<end && nums[start]==nums[start+1]){
                    start+=1
                }
                start+=1
            }
        }
    }
    return answer
    
};