/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function (nums, k) {
  let [start, end] = [0, nums.length - 1];
  nums.sort((a, b) => a - b);
  console.log(nums);
  let answer = 0;
  while (end > start) {
    let total = nums[start] + nums[end];
    if (total === k) {
      answer += 1;
      start += 1;
      end -= 1;
    } else if (total > k) {
      end -= 1;
    } else {
      start += 1;
    }
  }
  return answer;
};
