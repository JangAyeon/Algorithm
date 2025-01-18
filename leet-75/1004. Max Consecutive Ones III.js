/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function (nums, k) {
  let maxLen = 0;
  let l = 0;
  let zeros = 0;
  console.log(zeros);
  for (let r = 0; r < nums.length; r++) {
    if (nums[r] == 0) {
      zeros += 1;
    }
    while (zeros > k) {
      if (nums[l] == 0) {
        zeros -= 1;
      }
      l += 1;
    }
    const len = r - l + 1;
    maxLen = Math.max(maxLen, len);
  }
  return maxLen;
};
