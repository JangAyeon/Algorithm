/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  let idx = 0; // 요소의 값이 0인 인덱스를 저장한다.
  for (let i = 0; i < nums.length; i++) {
    let temp = 0;
    if (nums[i] !== 0) {
      // 0이 아닌 숫자이면 idx 위치의 0과 스왑한다.
      temp = nums[i];
      nums[i] = 0;
      nums[idx] = temp;
      idx++;
    }
  }
};
