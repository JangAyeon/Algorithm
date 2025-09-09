function solution(nums) {
    const nums_set = new Set(nums)
    console.log(nums_set.size)
    var answer = Math.min(nums_set.size, nums.length/2)
    return answer;
}