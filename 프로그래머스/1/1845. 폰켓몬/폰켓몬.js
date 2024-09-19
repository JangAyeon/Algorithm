function solution(nums) {
    const arr = []
    for (let num of nums){
        if (!arr.includes(num)){
            arr.push(num)
        }
    }
    const n = Math.min(arr.length, nums.length/2)
    console.log(arr,n)
    
    for(let i=n;i>0;i--){
        console.log(i)
    }
    return n
}