/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function (nums) {
  const pre_ = [0];

  for (let i = 0; i < nums.length; i++) {
    pre_.push(pre_[i] + nums[i]);
  }
  //console.log(pre_)
  let [l, r] = [pre_[0], pre_[pre_.length - 1]];
  let pivot = 1;
  for (; pivot < pre_.length; pivot++) {
    l = pre_[pivot - 1];
    r = pre_[pre_.length - 1] - pre_[pivot];
    //console.log(pivot, l,r)
    if (r == l) {
      return pivot - 1;
    }
  }
  return -1;
};
