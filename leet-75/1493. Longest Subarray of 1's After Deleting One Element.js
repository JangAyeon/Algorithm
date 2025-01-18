/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function (nums) {
  let l = 0;
  let maxLen = 0;
  let zeros = 0;
  let answer = 0;
  for (let r = 0; r < nums.length; r++) {
    if (nums[r] === 0) {
      zeros += 1;
    }
    while (zeros > 1) {
      if (nums[l] === 0) {
        zeros -= 1;
      }
      l += 1;
    }
    const len = r - l + 1;
    const subarray = zeros <= 1 ? len - 1 : len;
    answer = Math.max(answer, subarray);
    //console.log(l,r, zeros, r-l+1, subarray, answer)
  }
  return answer;
};
