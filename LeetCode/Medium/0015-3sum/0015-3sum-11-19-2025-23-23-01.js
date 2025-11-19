/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const answer = []
    nums.sort((a, b) => a - b)
    const n = nums.length
    // const visited =[]

    for (let i = 0; i < n - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue
        let [start, end, count] = [i + 1, n - 1, 0]
        const target = -nums[i]
        while (start < end) {
            const sum = nums[start] + nums[end]
            if (sum == target) {
                answer.push([nums[i], nums[start], nums[end]])
                console.log(nums[i], nums[start], nums[end])
                console.log(i, start, end)
                console.log()


                while (nums[start] == nums[start + 1]) {
                    start++
                }
                while (nums[end] == nums[end + 1]) {
                    end--
                }
                start++
                end--
            } else if (sum < target) {
                start++
            } else {
                end--
            }



        }
        // visited.push(nums[i])

    }
    console.log(answer)
    return answer
};