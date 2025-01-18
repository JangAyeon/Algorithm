/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function (nums1, nums2) {
  nums1 = new Set(nums1);
  nums2 = new Set(nums2);
  const temp1 = [...nums1].filter((e) => !nums2.has(e));
  const temp2 = [...nums2].filter((e) => !nums1.has(e));
  const answer = [temp1, temp2];
  return answer;
};
