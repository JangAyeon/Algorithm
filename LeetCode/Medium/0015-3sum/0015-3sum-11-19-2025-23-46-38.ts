function threeSum(nums: number[]): number[][] {
    const N = nums.length
    nums.sort((a,b)=>a-b)
    function binarySearch(l,r,t){
        let res = []
        const sum = nums[l]+nums[r]
        if(sum<t){
            binarySearch(l+1, r, t)
        }else{
            if(sum==t){
                console.log(l,r)
                res.push([l,r])
            }
            binarySearch(l,r-1,t)
        }

    }
    for(let i=0;i<N-2;i++){
        let [L,R] = [i+1, N-1]
        while(nums[i]==nums[L]){
            L++
        }
        binarySearch(L,R, 0-(nums[i]))
    }
    return [[0,0,0]]
};