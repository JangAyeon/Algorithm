/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    nums =  nums.map((item, idx)=>[item,idx])
    nums.sort((a,b)=>a[0]-b[0])
    console.log(nums)
    const N = nums.length
    let [L,R] = [0,N-1]
    const answer = []
    while(L<R){
        const sum =  (nums[L][0]+nums[R][0])
        if(sum>target){
            R-=1
        }
        else if(sum<target){
            L+=1
        }else{
            return ([nums[L][1], nums[R][1]])
            L+=1
            while(L<R && nums[L][0]==nums[L-1][0]){
                L+=1
            }
        }
    }
    console.log(answer)
    return answer
};