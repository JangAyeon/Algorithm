/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {

    const N = nums.length
    nums.sort((a,b)=>a-b)
    let answer = []
    for(let i=0;i<N;i++){
        if(i>0 && nums[i]==nums[i-1]){continue}
        let [L, R] = [i+1, N-1]
        const target = 0 - (nums[i])
        // binary Search
        while(L<R){
            const sum = nums[L]+nums[R]
            if(sum<target){
                L+=1
            }
            else if(sum>target){
                R-=1
            }
            else{
                answer.push([nums[i],nums[L],nums[R]])
                L+=1
                while(nums[L]==nums[L-1] && L<R){
                    L+=1
                }
            }
        }
    }
    console.log(answer)
    return answer
    
};